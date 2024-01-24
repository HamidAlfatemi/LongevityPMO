from django.shortcuts import render
from .models import Node, Edge
from django.db import connection
from django.db.models import Q
from django.db.models import F, ExpressionWrapper, fields

def network_graph(request):
    nodes_with_surface = Node.objects.annotate(
    surface=ExpressionWrapper(F('width') * F('height'), output_field=fields.IntegerField())
    )

    nodes = Node.objects.all() # nodes_with_surface.order_by('-surface')
    # nodes = Node.objects.filter(container=7)
    vindex = 0
    for node in nodes:
        # vindex = vindex + 1
        node.style = determine_style(node.nodeshape, node.nodecolor, node.dash, node.width, node.height, node.nodecaption) # vindex)
    
    edges = Edge.objects.all()
    # edges = Edge.objects.exclude(Q(begin__nodeshape=7) | Q(end__nodeshape=7))
    for edge in edges:
        edge.style = edge_style(edge.edgeshape, edge.color, edge.edgetype)
        # edge.style = 'edge_style_' + str(edge.edgeshape)  # Use a class name based on edgeshape

    return render(request, 'template.html', {'nodes': nodes, 'edges': edges})
    

def determine_style(nodeshape, nodecolor, dash, width, height, nodecaption): # vindex):
    shape_styles = {
        1: {'shape': 'rectangle'},
        2: {'shape': 'polygon', 'shape-polygon-points': '-1, -0.3,   1, -1,   1, 1,   -1, 1', 'height': '130px', 'text-margin-x': '7px', 'text-margin-y': '15px'},
        3: {'shape': 'polygon', 'shape-polygon-points': '-1, -1,   1, -0.3,   1, 1,   -1, 1', 'height': '130px', 'text-margin-x': '-6px', 'text-margin-y': '15px'},
        4: {'shape': 'polygon', 'shape-polygon-points': '-1, -1,   0.31, -1,   1, -0.3,   1, 0.3,   0.31, 1,   -1, 1', 'height': '115px', 'text-margin-x': '-6px'},
        5: {'shape': 'polygon', 'shape-polygon-points': '-1, -1,   0.31, -1,   1, -0.3,   1, 0.3,   0.31, 1,   -1, 1', 'height': '115px', 'text-margin-x': '-6px'},
        6: {'shape': 'ellipse'},
        7: {'shape': 'round-rectangle'}
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
        9: {'border-color': '#000000'} # Black
    }

    border_styles = {
        0: {'border-style': 'solid'},
        1: {'border-style': 'dashed'}
    }
    
    dimensions_styles = { 'width': width, 'height': height, 'text-max-width': len(nodecaption)*2.05 } # , 'z-index': vindex }
    
    shape_style = shape_styles.get(nodeshape, {'shape': 'rectangle'})
    color_style = color_styles.get(nodecolor, {'border-color': '#000000'})
    border_style = border_styles.get(dash, {'border-style': 'solid'})
    
    return {**shape_style, **color_style, **border_style, **dimensions_styles}

def edge_style(edgeshape, color, edgetype):
    width_styles = {
        1: {'width': 6},
        2: {'width': 15},
        3: {'width': 15, 'line-style': 'dotted'}
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
        0: {'target-arrow-shape': 'triangle'},
        1: {'target-arrow-shape': 'tee', 'target-arrow-color': '#00BB00'},
        2: {'target-arrow-shape': 'tee', 'target-arrow-color': '#EE0000'},
        3: {'target-arrow-shape': 'tee', 'target-arrow-color': '#000000'}
    }
    
    width_style = width_styles.get(edgeshape, {'width': 5})
    linecolor_style = linecolor_styles.get(color, {'line-color': '#000000'})
    arrow_style=arrow_styles.get(edgetype, {'target-arrow-shape': 'triangle'})

    return {**width_style, **linecolor_style, **arrow_style}
