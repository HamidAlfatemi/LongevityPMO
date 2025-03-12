from django.shortcuts import render
from django.shortcuts import redirect
from .models import Node, Edge
from django.db import connection
from django.db.models import Q
from django.db.models import F, ExpressionWrapper, fields
from collections import defaultdict, deque

def legend(request):
    return render(request, 'legend.html')

def index(request):
    return render(request, 'index.html')


def get_color_mappings():
    color_mapping = {
        1: "#0000DD", 2: "#CC9900", 3: "#3399FF", 4: "#993300",
        5: "#FF33CC", 6: "#00BB00", 7: "#9900CC", 8: "#EE0000",
        9: "#000000", 10: "#FF8000", 11: "#FFFF00",
    }
    light_color_mapping = {
        1: "#B7B7FF", 2: "#FFE69F", 3: "#B9DCFF", 4: "#FFCFB7",
        5: "#FFCDF2", 6: "#B7FFB7", 7: "#E9ABFF", 8: "#FFB3B3",
        9: "#CCCCCC", 10: "#FFC58B", 11: "#FFFFAA",
    }
    return color_mapping, light_color_mapping

def get_container_level(container_id, containers_dict):
    level = 0
    while container_id in containers_dict:
        container_id = containers_dict[container_id].parent_n_id
        level += 1
    return level

def prepare_container_hierarchy():
    # Get all container records and non-container nodes
    containers = Node.objects.filter(nodeshape=7).order_by('ref_num')
    nodes = Node.objects.exclude(nodeshape=7).order_by('ref_num')

    grouped_nodes = defaultdict(list)
    grouped_containers = defaultdict(list)
    containers_dict = {}

    # For each container, get its child nodes and child containers
    for container in containers:
        child_nodes = Node.objects.filter(parent_n_id=container.node_id).exclude(nodeshape=7).order_by('ref_num')
        child_containers = Node.objects.filter(parent_n_id=container.node_id, nodeshape=7).order_by('ref_num')
        grouped_nodes[container.node_id] = list(child_nodes)
        grouped_containers[container.node_id] = list(child_containers)

    # Build a dictionary of containers by node_id
    for container in containers:
        containers_dict[container.node_id] = container

    # Calculate levels for each container
    for container in containers:
        container.level = get_container_level(container.node_id, containers_dict)
        container.childlevel = container.level + 1

    # Separate containers by level
    containers_l1 = {container.node_id: container for container in containers if container.level == 1}
    containers_l2 = {container.node_id: container for container in containers if container.level == 2}
    containers_l3 = {container.node_id: container for container in containers if container.level == 3}
    containers_l4 = {container.node_id: container for container in containers if container.level == 4}

    return {
        'containers': containers,
        'nodes': nodes,
        'grouped_nodes': grouped_nodes,
        'grouped_containers': grouped_containers,
        'containers_dict': containers_dict,
        'containers_l1': containers_l1,
        'containers_l2': containers_l2,
        'containers_l3': containers_l3,
        'containers_l4': containers_l4,
    }

def containerlist(request):
    #nodes = Node.objects.filter(nodeshape=7)
    data = prepare_container_hierarchy()
    color_mapping, light_color_mapping = get_color_mappings()
    grouped_nodes = data['grouped_nodes']
    grouped_containers = data['grouped_containers']
    containers = data['containers']
    nodes = data['nodes']
    containers_l1 = data['containers_l1']
    containers_l2 = data['containers_l2']
    containers_l3 = data['containers_l3']
    containers_l4 = data['containers_l4']
    return render(request, 'containerlist.html',{
        #'nodes': nodes,
        'color_mapping': color_mapping,
        'light_color_mapping': light_color_mapping,
        'grouped_nodes': grouped_nodes,
        'grouped_containers': grouped_containers,
        'containers': containers,
        'containers_l1': containers_l1,
        'containers_l2': containers_l2,
        'containers_l3': containers_l3,
        'containers_l4': containers_l4,
    })
    
def process_selected_containers(request):
    if request.method == "POST":
        selected_container_ids = request.POST.getlist('selected_containers')
        selected_container_ids = list(map(int, selected_container_ids))  # Convert to int
        selected_containers = Node.objects.filter(node_id__in=selected_container_ids).order_by('ref_num')

        # Get hierarchy data using helper function
        data = prepare_container_hierarchy()
        grouped_nodes = data['grouped_nodes']
        grouped_containers = data['grouped_containers']
        containers = data['containers']
        containers_l1 = data['containers_l1']
        containers_l2 = data['containers_l2']
        containers_l3 = data['containers_l3']
        containers_l4 = data['containers_l4']
        
        child_node_ids = Node.objects.filter(parent_n__in=selected_containers).exclude(nodeshape=7).values_list('node_id', flat=True)
        selected_node_ids = list(child_node_ids) + selected_container_ids

        color_mapping, light_color_mapping = get_color_mappings()
        
        renderview = "containers"
        
        return render(request, 'nodelist.html', {
            'containers': containers,
            'containers_l1': containers_l1,
            # 'containers_l2': containers_l2,
            # 'containers_l3': containers_l3,
            # 'containers_l4': containers_l4,
            'grouped_nodes': grouped_nodes,
            'grouped_containers': grouped_containers,
            'selected_node_ids': selected_node_ids,
            'selected_container_ids': selected_container_ids,
            'color_mapping': color_mapping,
            'light_color_mapping': light_color_mapping,
            'renderview': renderview,
        })

    return redirect('containerlist')  # Redirect back if not a POST request

def node_to_node(request):
    selected_container_ids = []
    selected_containers = []
    data = prepare_container_hierarchy()
    grouped_nodes = data['grouped_nodes']
    grouped_containers = data['grouped_containers']
    containers = data['containers']
    containers_l1 = data['containers_l1']
        
    selected_node_ids = []

    color_mapping, light_color_mapping = get_color_mappings()

    renderview = "nodetonode"
        
    return render(request, 'nodelist.html', {
        'containers': containers,
        'containers_l1': containers_l1,
        'grouped_nodes': grouped_nodes,
        'grouped_containers': grouped_containers,
        'selected_node_ids': selected_node_ids,
        'selected_container_ids': selected_container_ids,
        'color_mapping': color_mapping,
        'light_color_mapping': light_color_mapping,
        'renderview': renderview,
    })

def one_node(request):
    selected_container_ids = []
    selected_containers = []
    data = prepare_container_hierarchy()
    grouped_nodes = data['grouped_nodes']
    grouped_containers = data['grouped_containers']
    containers = data['containers']
    containers_l1 = data['containers_l1']
        
    selected_node_ids = []

    color_mapping, light_color_mapping = get_color_mappings()

    renderview = "onenode"
        
    return render(request, 'nodelist.html', {
        'containers': containers,
        'containers_l1': containers_l1,
        'grouped_nodes': grouped_nodes,
        'grouped_containers': grouped_containers,
        'selected_node_ids': selected_node_ids,
        'selected_container_ids': selected_container_ids,
        'color_mapping': color_mapping,
        'light_color_mapping': light_color_mapping,
        'renderview': renderview,
    })


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

def determine_style(nodeshape, nodecolor, dash, width, height, nodecaption):
    shape_styles = { # define style based on node.nodeshape
        1: {'shape': 'rectangle', 'width': width, 'height': height, 'text-max-width': len(nodecaption)*2.05, 'border-width': 10, 'text-valign': 'center', 'text-halign': 'center', 'background-color': '#fff', 'color': '#000', 'text-wrap': 'wrap'},
        2: {'shape': 'polygon', 'shape-polygon-points': '-1, -0.3,   1, -1,   1, 1,   -1, 1', 'height': '130px', 'text-margin-x': '7px', 'text-margin-y': '15px', 'width': width, 'height': height, 'text-max-width': len(nodecaption)*2.05, 'border-width': 10, 'text-valign': 'center', 'text-halign': 'center', 'background-color': '#fff', 'color': '#000', 'text-wrap': 'wrap'},
        3: {'shape': 'polygon', 'shape-polygon-points': '-1, -1,   1, -0.3,   1, 1,   -1, 1', 'height': '130px', 'text-margin-x': '-6px', 'text-margin-y': '15px', 'width': width, 'height': height, 'text-max-width': len(nodecaption)*2.05, 'border-width': 10, 'text-valign': 'center', 'text-halign': 'center', 'background-color': '#fff', 'color': '#000', 'text-wrap': 'wrap'},
        4: {'shape': 'polygon', 'shape-polygon-points': '-1, -1,   0.31, -1,   1, -0.3,   1, 0.3,   0.31, 1,   -1, 1', 'height': '115px', 'text-margin-x': '-6px', 'width': width, 'height': height, 'text-max-width': len(nodecaption)*2.05, 'border-width': 10, 'text-valign': 'center', 'text-halign': 'center', 'background-color': '#fff', 'color': '#000', 'text-wrap': 'wrap'},
        5: {'shape': 'polygon', 'shape-polygon-points': '-1, -0.3,   -0.31, -1,   1, -1,   1, 1,   -0.31, 1,   -1, 0.3', 'height': '115px', 'text-margin-x': '-6px', 'width': width, 'height': height, 'text-max-width': len(nodecaption)*2.05, 'border-width': 10, 'text-valign': 'center', 'text-halign': 'center', 'background-color': '#fff', 'color': '#000', 'text-wrap': 'wrap', 'text-margin-x': '10px'},
        6: {'shape': 'ellipse', 'width': width, 'height': height, 'text-max-width': len(nodecaption)*2.05, 'border-width': 10, 'text-valign': 'center', 'text-halign': 'center', 'background-color': '#fff', 'color': '#000', 'text-wrap': 'wrap'},
        7: {'shape': 'round-rectangle', 'border-width': 10, 'text-valign': 'top', 'text-margin-y': '100px', 'text-halign': 'center', 'color': '#000', 'text-wrap': 'wrap', 'font-weight': 'bold', 'font-size': '40px', 'padding': '100px'}
    }

    color_styles = { # define color based on node.nodecolor
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

    border_styles = { # define border style based on node.dashed
        0: {'border-style': 'solid'},
        1: {'border-style': 'dashed'}
    }
    
    shape_style = shape_styles.get(nodeshape, {'shape': 'rectangle'})
    color_style = color_styles.get(nodecolor, {'border-color': '#000000'}) # default border color is black
    border_style = border_styles.get(dash, {'border-style': 'solid'})
    
    if nodeshape == 7: # node is a container
        background_color = get_lighter_color(nodecolor)  # lighter color of boders for the background of the containers
        shape_style['background-color'] = background_color

    return {**shape_style, **color_style, **border_style}

def edge_style(edgeshape, color, edgetype):
    width_styles = { # define width and pattern of the Edge based on edge.edgeshape
        1: {'width': 6},
        2: {'width': 15},
        3: {'width': 15, 'line-style': 'dotted'}
    }

    linecolor_styles = { # define color of the Edge based on edge.color
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

    arrow_styles = { # define arrow head of the Edge based on edge.edgetype
        1: {'target-arrow-shape': 'triangle'},
        2: {'target-arrow-shape': 'tee', 'target-arrow-color': '#00BB00'},
        3: {'target-arrow-shape': 'tee', 'target-arrow-color': '#EE0000'},
        4: {'target-arrow-shape': 'tee', 'target-arrow-color': '#000000'}
    }
    
    width_style = width_styles.get(edgeshape, {'width': 5})
    linecolor_style = linecolor_styles.get(color, {'line-color': '#000000'})
    arrow_style=arrow_styles.get(edgetype, {'target-arrow-shape': 'triangle'})

    return {**width_style, **linecolor_style, **arrow_style}

# def get_all_paths(graph, start, goal, path=None):
    # """
    # Recursive DFS: Returns a list of all paths (each a list of node IDs)
    # from start to goal in the graph.
    # """
    # if path is None:
        # path = []
    # path = path + [start]
    # if start == goal:
        # return [path]
    # if start not in graph:
        # return []
    # paths = []
    # for node in graph[start]:
        # if node not in path:  # avoid cycles
            # newpaths = get_all_paths(graph, node, goal, path)
            # for newpath in newpaths:
                # paths.append(newpath)
    # return paths

def bfs_shortest_path(graph, start, goal):
    """
    Return the shortest path from start to goal using BFS.
    The graph is a dictionary mapping each node ID to a list of adjacent node IDs.
    If no path exists, returns None.
    """
    # Queue for BFS: each element is a path (list of node IDs)
    queue = deque([[start]])
    # Mark the start node as visited
    visited = {start}
    
    while queue:
        # Get the current path from the queue
        path = queue.popleft()
        node = path[-1]
        
        # If we've reached the goal, return the path
        if node == goal:
            return path
        
        # Otherwise, explore the neighbors
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [neighbor]
                queue.append(new_path)
    
    # No path found
    return None

from collections import deque

def get_reachable_nodes(graph, start):
    """
    Returns a set of all node IDs reachable from 'start' in the given 'graph'
    using a breadth-first search.
    """
    visited = set()
    queue = deque([start])
    while queue:
        current = queue.popleft()
        if current not in visited:
            visited.add(current)
            for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    queue.append(neighbor)
    return visited

def build_graph(edges):
    """
    Build a forward graph from edges.
    Returns a dictionary mapping node IDs to a list of adjacent node IDs.
    """
    graph = {}
    for edge in edges:
        s = edge.begin.node_id
        e = edge.end.node_id
        if s not in graph:
            graph[s] = []
        graph[s].append(e)
    return graph

def build_reverse_graph(edges):
    """
    Build a reverse graph from edges.
    Returns a dictionary mapping node IDs to a list of preceding node IDs.
    """
    reverse_graph = {}
    for edge in edges:
        s = edge.begin.node_id
        e = edge.end.node_id
        if e not in reverse_graph:
            reverse_graph[e] = []
        reverse_graph[e].append(s)
    return reverse_graph

def sbha(request):
    if request.method == 'POST':
        # Retrieve the list of selected node IDs from the request
        selected_node_ids = request.POST.getlist('selected_nodes')

        # Check if the "Include Containers" checkbox is checked
        include_containers = request.POST.get('include_containers')  # Returns None if unchecked
        
        #nodes = all_nodes.exclude(nodeshape=7)
        nodes = Node.objects.filter(node_id__in=selected_node_ids)
        
        extra_paths = []  # Will store DFS results if applicable

        renderview = request.POST.get('renderview', '')
        #print(renderview)
        if renderview == 'nodetonode':
            # Ensure exactly two nodes are selected
            if nodes.count() != 2:
                return HttpResponse("For 'nodetonode' view, please select exactly two nodes.")
            else:
                node_list = list(nodes)
                start_node_id = node_list[0].node_id
                end_node_id = node_list[1].node_id

                # Build an adjacency list from all edges in the database.
                all_edges = Edge.objects.all()
                graph = {}
                for edge in all_edges:
                    s = edge.begin.node_id
                    e = edge.end.node_id
                    if s not in graph:
                        graph[s] = []
                    graph[s].append(e)

                # # Use DFS to find all paths from start_node_id to end_node_id.
                # extra_paths = get_all_paths(graph, start_node_id, end_node_id)
                # # Optionally, you could convert node IDs in each path to Node objects.

                # # Collect all node IDs appearing in any path
                # extra_node_ids = set()
                # for path in extra_paths:
                    # for nid in path:
                        # extra_node_ids.add(nid)

                # Use BFS to find the shortest path from start_node_id to end_node_id.
                shortest_path = bfs_shortest_path(graph, start_node_id, end_node_id)
                if shortest_path is None:
                    # If no path is found, you might want to handle it appropriately.
                    return HttpResponse("No path found between the two nodes.")

                ## Combine with the originally selected two nodes (if not already included)
                #combined_node_ids = set([start_node_id, end_node_id]) | extra_node_ids
                # Collect all node IDs in the shortest path.
                combined_node_ids = set(shortest_path)
                
                all_node_ids = set(combined_node_ids)  # Start with current set

                for nid in list(combined_node_ids):
                    node_obj = Node.objects.filter(node_id=nid).first()
                    # Traverse upward through the parent chain.
                    while node_obj and node_obj.parent_n_id:
                        parent_id = node_obj.parent_n_id
                        all_node_ids.add(parent_id)
                        node_obj = Node.objects.filter(node_id=parent_id).first()
                
                # Re-query the Node table to get all nodes in the union
                #nodes = Node.objects.filter(node_id__in=combined_node_ids)
                nodes = Node.objects.filter(node_id__in=all_node_ids)

        
            
        if renderview == 'onenode':
            if nodes.count() != 1:
                return HttpResponse("For 'onenode' view, please select exactly one node.")
            else:
                node_list = list(nodes)
                start_node_id = node_list[0].node_id

                # Build graphs from all edges.
                all_edges = Edge.objects.all()
                graph = build_graph(all_edges)
                reverse_graph = build_reverse_graph(all_edges)

                # If neither upstream nor downstream is selected, don't proceed.
                if not request.POST.get('downstream') and not request.POST.get('upstream'):
                    return HttpResponse("Please select at least one option (upstream and/or downstream).")

                # Start with the selected node.
                final_ids = {start_node_id}
                
                # If the downstream checkbox is checked, include all reachable downstream nodes.
                if request.POST.get('downstream'):
                    downstream_ids = get_reachable_nodes(graph, start_node_id)
                    final_ids = final_ids.union(downstream_ids)
                
                # If the upstream checkbox is checked, include all reachable upstream nodes.
                if request.POST.get('upstream'):
                    upstream_ids = get_reachable_nodes(reverse_graph, start_node_id)
                    final_ids = final_ids.union(upstream_ids)
                
                all_node_ids = set(final_ids)
                for nid in list(final_ids):
                    node_obj = Node.objects.filter(node_id=nid).first()
                    while node_obj and node_obj.parent_n_id:
                        parent_id = node_obj.parent_n_id
                        all_node_ids.add(parent_id)
                        node_obj = Node.objects.filter(node_id=parent_id).first()
                
                nodes = Node.objects.filter(node_id__in=all_node_ids)
                
        if include_containers:
            container_count = nodes.filter(nodeshape=7).count()
        else:
            container_count = 0
            nodes = nodes.exclude(nodeshape=7)

        # Apply styles to the nodes
        for node in nodes:
            node.style = determine_style(node.nodeshape, node.nodecolor, node.dashed, node.width, node.height, node.nodecaption) # create each node styled based on attributes in the record

        # Filter edges where both endpoints are in the selected nodes
        edges = Edge.objects.filter(begin_id__in=nodes.values_list('node_id', flat=True), end_id__in=nodes.values_list('node_id', flat=True)) # only edges with both side nodes present
    
        # Apply styles to the edges
        for edge in edges:
            edge.style = edge_style(edge.edgeshape, edge.color, edge.edgetype) # create each edge styled based on attributes in the record

        # Count the number of selected nodes
        node_count = nodes.exclude(nodeshape=7).count()
        edge_count = edges.count()

        if include_containers:
            calculated_width = (14.3 * node_count + 1310)
            calculated_height = (31.3 * node_count + 643)*2
        else:
            calculated_width = (14.3 * node_count + 1310)*.67
            calculated_height = (31.3 * node_count + 643)

        return render(request, 'sbha.html', {
            'nodes': nodes,
            'edges': edges,
            'node_count': node_count,
            'edge_count': edge_count,
            'container_count': container_count,
            'calculated_width': calculated_width,
            'calculated_height': calculated_height,
        })
    else:
        # If the request is not POST, handle the scenario (optional)
        return HttpResponse("Invalid request method. Please submit the form.")
        
