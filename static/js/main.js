// =================== Cytoscape Graph ===================
document.addEventListener('DOMContentLoaded', function() {
    const dataElement = document.getElementById('graph-data');
    if (!dataElement) return;

    const graphData = JSON.parse(dataElement.dataset.json);
    const cyDiv = document.getElementById('cy');

    // Set calculated size dynamically
    cyDiv.style.width = cyDiv.dataset.width + 'px';
    cyDiv.style.height = cyDiv.dataset.height + 'px';

    // Initialize Cytoscape
    cytoscape({
        container: cyDiv,
        elements: { nodes: graphData.nodes, edges: graphData.edges },
        layout: { name: 'cola', flow: 'x', animate: false },
        style: [
            { selector: 'node', style: { 'label': 'data(label)' } },
            { selector: 'edge', style: { 'curve-style': 'bezier', 'line-opacity': 0.63 } }
        ]
    });
});

// =================== Read More / Read Less ===================
document.addEventListener("DOMContentLoaded", function () {
    const btn = document.getElementById('readMoreBtn');
    const content = document.getElementById('readMoreContent');
    if (btn && content) {
        btn.addEventListener('click', function () {
            content.classList.toggle('visible');
            btn.textContent = content.classList.contains('visible') ? 'Read Less ▲' : 'Read More ▼';
        });
    }
});


// =================== Smooth Scrolling for Internal Anchors ===================
document.addEventListener("DOMContentLoaded", function () {
    if (window.location.hash) {
        const element = document.querySelector(window.location.hash);
        if (element) {
            setTimeout(() => {
                element.scrollIntoView({ behavior: "smooth" });
            }, 100);
        }
    }
});


// =================== Nodelist Page Logic ===================
document.addEventListener("DOMContentLoaded", () => {
    const nodesTree = document.getElementById("nodesTree");
    if (!nodesTree) return; // Only run this section on nodelist.html

    const containerCheckboxes = document.querySelectorAll('input[type="checkbox"][name="selected_nodes"]');
    const dpbutton = document.getElementById("drawPathwayButton");
    const renderview = document.body.dataset.renderview || "{{ renderview }}"; // fallback if added later
    let maxSelection = (renderview === "nodetonode") ? 2 : 1;
    let selectedCount = 0;

    function updateSelectionCount() {
        selectedCount = [...containerCheckboxes].filter(cb => cb.checked).length;
    }

    containerCheckboxes.forEach((checkbox) => {
        checkbox.addEventListener("click", (event) => {
            if (renderview === "nodetonode" || renderview === "onenode") {
                if (event.target.checked) {
                    updateSelectionCount();
                    if (selectedCount === maxSelection) {
                        setTimeout(() => dpbutton.scrollIntoView({ behavior: "smooth", block: "end" }), 500);
                    }
                    if (selectedCount > maxSelection) {
                        event.preventDefault();
                        updateSelectionCount();
                        return;
                    }
                }
                setTimeout(updateSelectionCount, 0);
            } else {
                const containerId = event.target.value;
                toggleChildren(containerId, event.target.checked);
            }
        });
    });

    // Select All / Deselect All Buttons
    const selectAllButton = document.getElementById('selectAllButton');
    if (selectAllButton) {
        selectAllButton.addEventListener('click', function() {
            document.querySelectorAll('input[name="selected_nodes"]').forEach(cb => cb.checked = true);
        });
    }

    const deselectAllButton = document.getElementById('deselectAllButton');
    if (deselectAllButton) {
        deselectAllButton.addEventListener('click', function() {
            document.querySelectorAll('input[name="selected_nodes"]').forEach(cb => cb.checked = false);
        });
    }

    // Search Filtering
    const searchInput = document.getElementById("searchInput");
    if (searchInput) {
        searchInput.addEventListener("keypress", function (event) {
            if (event.key === "Enter") {
                event.preventDefault();
                filterTable();
            }
        });
    }


    window.filterTable = function() {
        const filter = searchInput.value.toLowerCase();
        const rows = document.querySelectorAll(".tree li");
        const visibleContainers = new Set();

        rows.forEach(row => {
            const isContainer = row.classList.contains("container-row");
            const text = row.textContent.toLowerCase();
            if (isContainer) {
                row.style.display = "none";
            } else {
                const parentId = row.getAttribute("data-parent-id");
                if (text.includes(filter)) {
                    row.style.display = "";
                    visibleContainers.add(parentId);
                } else {
                    row.style.display = "none";
                }
            }
        });

        rows.forEach(row => {
            if (row.classList.contains("container-row")) {
                const containerId = row.getAttribute("data-container-id");
                const text = row.textContent.toLowerCase();
                if (visibleContainers.has(containerId) || text.includes(filter)) {
                    row.style.display = "";
                }
            }
        });
    };

    window.removefilter = function() {
        searchInput.value = "";
        document.querySelectorAll(".tree li").forEach(row => row.style.display = "");
    };
    // Added by ChatGPT
	const searchButton = document.getElementById("searchButton");
    const removeFilterButton = document.getElementById("removefilter");

    if (searchButton) {
        searchButton.addEventListener("click", filterTable);
    }

    if (removeFilterButton) {
        removeFilterButton.addEventListener("click", removefilter);
    }
    // End of added by ChatGPT

    // Tree expand/collapse
    window.toggleVisibility = function(containerId) {
        const pcontainer = document.getElementById('container-' + containerId);
        const children = pcontainer.querySelector('.children');
        const arrow = pcontainer.querySelector('.collapsible .arrow');
        if (children.style.display === 'block' || children.style.display === '') {
            children.style.display = 'none';
            arrow.textContent = '\u25B6';
        } else {
            children.style.display = 'block';
            arrow.textContent = '\u25BC';
        }
    };

    window.toggleVisibility_l2 = function(containerId) {
        const pcontainer = document.getElementById('container-' + containerId);
        const children = pcontainer.querySelector('.children');
        const arrow = pcontainer.querySelector('.collapsible .arrow');
        if (!children || !arrow) return;
        const visible = (children.style.display === 'block' || children.style.display === '');
        children.style.display = visible ? 'none' : 'block';
        arrow.textContent = visible ? '\u25B6' : '\u25BC';
    };

    window.toggleVisibility_l3 = function(containerId) {
        const pcontainer = document.getElementById('container-' + containerId);
        const children = pcontainer.querySelector('.children');
        const arrow = pcontainer.querySelector('.collapsible .arrow');
        if (!children || !arrow) return;
        const visible = (children.style.display === 'block' || children.style.display === '');
        children.style.display = visible ? 'none' : 'block';
        arrow.textContent = visible ? '\u25B6' : '\u25BC';
    };

    window.toggleChildren = function(containerId, isChecked) {
        const parentElement = document.querySelector(`#container-${containerId}`);
        if (parentElement) {
            const childCheckboxes = parentElement.querySelectorAll('input[type="checkbox"]');
            childCheckboxes.forEach(cb => cb.checked = isChecked);
        }
    };
});
document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.arrow').forEach(function (arrow) {
        arrow.addEventListener('click', function () {
            const level = this.dataset.level;
            const id = this.dataset.id;

            if (level === '1') {
                toggleVisibility(id);
            } else if (level === '2') {
                toggleVisibility_l2(id);
            } else if (level === '3') {
                toggleVisibility_l3(id);
            }
        });
    });
});

// ===== apply dynamic colours moved from inline styles =====
document.addEventListener("DOMContentLoaded", function () {
    // Apply border/background for container boxes (node-box)
    document.querySelectorAll('.node-box').forEach(el => {
        const border = el.dataset.nodeColor;       // e.g. "#ff0000" or color name
        const bg = el.dataset.lightNodeColor;      // e.g. "#ffeeee"
        if (border) el.style.borderColor = border;
        if (bg) el.style.backgroundColor = bg;
    });

    // Apply border/text color for node items (li)
    document.querySelectorAll('.node-item').forEach(li => {
        const c = li.dataset.nodeColor;
        if (c) {
            li.style.borderColor = c;
            li.style.color = c;
        }
    });

    // Ensure .ml-20 and .ml-40 exist for nested lists (if needed)
    // (no JS required; classes applied in HTML / CSS do the job)
});



// =================== Header Menu (Hamburger + Submenus) ===================
document.addEventListener('DOMContentLoaded', function () {
    const hamburger = document.querySelector('.hamburger');
    const navbar = document.querySelector('.navbar');

    if (hamburger && navbar) {
        hamburger.addEventListener('click', function () {
            navbar.classList.toggle('active');
        });
    }

    function toggleSubmenu(toggleElement) {
        const parentLi = toggleElement.parentElement;
        const allMenus = document.querySelectorAll('.menu > li');
        allMenus.forEach(menu => {
            if (menu !== parentLi) menu.classList.remove('active');
        });
        parentLi.classList.toggle('active');
    }

    const sbhaToggle = document.getElementById('sbhaToggle');
	// console.log('sbhaToggle found:', sbhaToggle);

    if (sbhaToggle) {
        sbhaToggle.addEventListener('click', function (e) {
            e.preventDefault();
            toggleSubmenu(sbhaToggle);
        });
    }

    const aboutToggle = document.getElementById('aboutToggle');
    if (aboutToggle) {
        aboutToggle.addEventListener('click', function (e) {
            e.preventDefault();
            toggleSubmenu(aboutToggle);
        });
    }

    // Close submenu when clicking outside the menu
    document.addEventListener('click', function (event) {
        const menus = document.querySelectorAll('.menu > li');
        let isClickInsideMenu = false;
        menus.forEach(menu => {
            if (menu.contains(event.target)) isClickInsideMenu = true;
        });
        if (!isClickInsideMenu) menus.forEach(menu => menu.classList.remove('active'));
    });

    // Close submenu when a submenu item is clicked
    document.querySelectorAll('.submenu a').forEach(item => {
        item.addEventListener('click', function () {
            document.querySelectorAll('.menu > li').forEach(menu => menu.classList.remove('active'));
        });
    });

    // Close navbar when clicking outside it
    document.addEventListener('click', function (event) {
        const hamburger = document.querySelector('.hamburger');
        const navbar = document.querySelector('.navbar');
        if (!hamburger.contains(event.target) && !navbar.contains(event.target)) {
            navbar.classList.remove('active');
        }
    });
});

// =================== Containerlist Page Logic ===================
document.addEventListener("DOMContentLoaded", function() {
    const containerForm = document.getElementById('containerForm');
    if (containerForm) {
        containerForm.addEventListener('submit', function(event) {
            const checkboxes = document.querySelectorAll('input[name="selected_containers"]:checked');
            if (checkboxes.length === 0) {
                event.preventDefault();
                const errorMessage = document.getElementById('error-message');
                errorMessage.style.display = 'block';
                setTimeout(() => {
                    errorMessage.style.display = 'none';
                }, 3000);
            }
        });
    }

    const selectAllButton = document.getElementById('selectAllButton');
    if (selectAllButton) {
        selectAllButton.addEventListener('click', function() {
            const checkboxes = document.querySelectorAll('input[name="selected_containers"]');
            checkboxes.forEach(checkbox => {
                checkbox.checked = true;
            });
        });
    }

    const deselectAllButton = document.getElementById('deselectAllButton');
    if (deselectAllButton) {
        deselectAllButton.addEventListener('click', function() {
            const checkboxes = document.querySelectorAll('input[name="selected_containers"]');
            checkboxes.forEach(checkbox => {
                checkbox.checked = false;
            });
        });
    }

    const containerCheckboxes = document.querySelectorAll('input[type="checkbox"][name="selected_containers"]');
    containerCheckboxes.forEach((checkbox) => {
        checkbox.addEventListener("change", (event) => {
            const containerId = event.target.value;
            toggleChildren(containerId, event.target.checked);
        });
    });

    // Apply color mappings for container boxes
    document.querySelectorAll('.container-box').forEach(box => {
        const border = box.dataset.border;
        const bg = box.dataset.bg;
        if (border) box.style.borderColor = border;
        if (bg) box.style.backgroundColor = bg;
    });
});

function toggleChildren(containerId, isChecked) {
    const parentElement = document.querySelector(`#container-${containerId}`);
    if (parentElement) {
        const childCheckboxes = parentElement.querySelectorAll('input[type="checkbox"]');
        childCheckboxes.forEach((checkbox) => {
            checkbox.checked = isChecked;
        });
    }
}
