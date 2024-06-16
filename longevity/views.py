from django.shortcuts import render
from .models import Node, Edge
from django.db import connection
from django.db.models import Q
from django.db.models import F, ExpressionWrapper, fields
import time

################### time measurement #################
#start_time = time.time()
#print(start_time)
######################################################

def network_graph(request):
    nodes = Node.objects.all()
    #nodes = Node.objects.filter(Q(ref_num='078') | Q(ref_num='160') | Q(ref_num='911') | Q(ref_num='913') | Q(ref_num='210') | Q(ref_num='209') | Q(ref_num='077') | Q(ref_num='432') | Q(ref_num='428') | Q(ref_num='423') | Q(ref_num='702') | Q(ref_num='720') | Q(ref_num='212') | Q(ref_num='719') | Q(ref_num='717') | Q(ref_num='081') | Q(ref_num='357') | Q(ref_num='711')) # | Q(ref_num='804') | Q(ref_num='807') | Q(ref_num='200') | Q(ref_num='801') | Q(ref_num='900'))
    for node in nodes:
        node.style = determine_style(node.nodeshape, node.nodecolor, node.dash, node.width, node.height, node.nodecaption)

    edges = Edge.objects.filter(begin_id__in=nodes.values_list('node_id', flat=True), end_id__in=nodes.values_list('node_id', flat=True))
    for edge in edges:
        edge.style = edge_style(edge.edgeshape, edge.color, edge.edgetype)

    return render(request, 'sbha.html', {'nodes': nodes, 'edges': edges})

################### time measurement #################
# end_time = time.time()
# print(end_time)
# elapsed_time = end_time - start_time
# print(f"Elapsed time: {elapsed_time:.2f} seconds - views.py")
######################################################

def determine_style(nodeshape, nodecolor, dash, width, height, nodecaption): # vindex):
    shape_styles = {
        1: {'shape': 'rectangle', 'width': width, 'height': height, 'text-max-width': len(nodecaption)*2.05, 'border-width': 10, 'text-valign': 'center', 'text-halign': 'center', 'background-color': '#fff', 'color': '#000', 'text-wrap': 'wrap'},
        2: {'shape': 'polygon', 'shape-polygon-points': '-1, -0.3,   1, -1,   1, 1,   -1, 1', 'height': '130px', 'text-margin-x': '7px', 'text-margin-y': '15px', 'width': width, 'height': height, 'text-max-width': len(nodecaption)*2.05, 'border-width': 10, 'text-valign': 'center', 'text-halign': 'center', 'background-color': '#fff', 'color': '#000', 'text-wrap': 'wrap'},
        3: {'shape': 'polygon', 'shape-polygon-points': '-1, -1,   1, -0.3,   1, 1,   -1, 1', 'height': '130px', 'text-margin-x': '-6px', 'text-margin-y': '15px', 'width': width, 'height': height, 'text-max-width': len(nodecaption)*2.05, 'border-width': 10, 'text-valign': 'center', 'text-halign': 'center', 'background-color': '#fff', 'color': '#000', 'text-wrap': 'wrap'},
        4: {'shape': 'polygon', 'shape-polygon-points': '-1, -1,   0.31, -1,   1, -0.3,   1, 0.3,   0.31, 1,   -1, 1', 'height': '115px', 'text-margin-x': '-6px', 'width': width, 'height': height, 'text-max-width': len(nodecaption)*2.05, 'border-width': 10, 'text-valign': 'center', 'text-halign': 'center', 'background-color': '#fff', 'color': '#000', 'text-wrap': 'wrap'},
        5: {'shape': 'polygon', 'shape-polygon-points': '-1, -0.3,   -0.31, -1,   1, -1,   1, 1,   -0.31, 1,   -1, 0.3', 'height': '115px', 'text-margin-x': '-6px', 'width': width, 'height': height, 'text-max-width': len(nodecaption)*2.05, 'border-width': 10, 'text-valign': 'center', 'text-halign': 'center', 'background-color': '#fff', 'color': '#000', 'text-wrap': 'wrap', 'text-margin-x': '10px'},
        6: {'shape': 'ellipse', 'width': width, 'height': height, 'text-max-width': len(nodecaption)*2.05, 'border-width': 10, 'text-valign': 'center', 'text-halign': 'center', 'background-color': '#fff', 'color': '#000', 'text-wrap': 'wrap'},
        7: {'shape': 'round-rectangle', 'border-width': 10, 'text-valign': 'top', 'text-margin-y': '100px', 'text-halign': 'center', 'color': '#000', 'text-wrap': 'wrap', 'font-weight': 'bold', 'font-size': '40px', 'padding': '100px'}
    }

    color_styles = {
        1: {'border-color': '#0000DD'}, # Blue
        2: {'border-color': '#CC9900'}, # Light Brown
        3: {'border-color': '#3399FF'}, # Light Blue
        4: {'border-color': '#993300'}, # Brown 
        5: {'border-color': '#FF33CC'}, # Pink 
        6: {'border-color': '#00BB00'}, # Green
        7: {'border-color': '#9900CC'}, # Purple 
        8: {'border-color': '#EE0000'}, # Red
        9: {'border-color': '#000000'}, # Black
        10: {'border-color': '#FF8000'}, # Orange
        11: {'border-color': '#FFFF00'} # Yellow
    }

    border_styles = {
        0: {'border-style': 'solid'},
        1: {'border-style': 'dashed'}
    }
    
    # dimensions_styles = { 'width': width, 'height': height, 'text-max-width': len(nodecaption)*2.05 } # , 'z-index': vindex }
    
    shape_style = shape_styles.get(nodeshape, {'shape': 'rectangle'})
    color_style = color_styles.get(nodecolor, {'border-color': '#000000'})
    border_style = border_styles.get(dash, {'border-style': 'solid'})
    
    if nodeshape == 7:
        #shape_style['background-color'] = color_style['border-color']
        #shape_style['background-opacity'] = 0.5
        background_color = get_lighter_color(nodecolor)  # Assuming you have a function to get lighter color
        shape_style['background-color'] = background_color
        #shape_style['classes'] = 'container-label'

    return {**shape_style, **color_style, **border_style} # , **dimensions_styles}

def edge_style(edgeshape, color, edgetype):
    width_styles = {
        1: {'width': 6},
        2: {'width': 15},
        3: {'width': 15, 'line-style': 'dotted'} #, 'target-arrow-opacity': 0.5}
    }

    linecolor_styles = {
        1: {'line-color': '#0000DD', 'target-arrow-color': '#0000DD'},  # Blue
        2: {'line-color': '#CC9900', 'target-arrow-color': '#CC9900'},  # Light Brown
        3: {'line-color': '#3399FF', 'target-arrow-color': '#3399FF'},  # Light Blue
        4: {'line-color': '#993300', 'target-arrow-color': '#993300'}, # Brown 
        5: {'line-color': '#FF33CC', 'target-arrow-color': '#FF33CC'}, # Pink 
        6: {'line-color': '#00BB00', 'target-arrow-color': '#00BB00'}, # Green
        7: {'line-color': '#9900CC', 'target-arrow-color': '#9900CC'}, # Purple 
        8: {'line-color': '#EE0000', 'target-arrow-color': '#EE0000'}, # Red
        9: {'line-color': '#000000', 'target-arrow-color': '#000000'} # Black
    }

    arrow_styles = {
        0: {'target-arrow-shape': 'triangle'}, # 'target-arrow-opacity': 0.63},
        1: {'target-arrow-shape': 'tee', 'target-arrow-color': '#00BB00'},
        2: {'target-arrow-shape': 'tee', 'target-arrow-color': '#EE0000'},
        3: {'target-arrow-shape': 'tee', 'target-arrow-color': '#000000'}
    }
    
    width_style = width_styles.get(edgeshape, {'width': 5})
    linecolor_style = linecolor_styles.get(color, {'line-color': '#000000'})
    arrow_style=arrow_styles.get(edgetype, {'target-arrow-shape': 'triangle'})

    return {**width_style, **linecolor_style, **arrow_style}

def get_lighter_color(nodecolor):
    lighter_colors = {
        1: '#B7B7FF',  # Blue
        2: '#FFE69F',  # Light Brown
        3: '#B9DCFF',  # Light Blue
        4: '#FFCFB7',  # Brown 
        5: '#FFCDF2',  # Pink 
        6: '#B7FFB7',  # Green
        7: '#E9ABFF',  # Purple 
        8: '#FFB3B3',  # Red
        9: '#CCCCCC',   # Black
        10: '#FFC58B',   # Orange
        11: '#FFFFAA'   # Yellow
    }
    return lighter_colors.get(nodecolor, '#FFFFFF')