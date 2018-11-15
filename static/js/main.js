var sidebarbuttons = document.querySelectorAll('[data-cmd="sidebarbutton"]');
var modalbuttons = document.querySelectorAll('[data-cmd="modalbutton"]');
var menuclosers = document.querySelectorAll('.close-button');
var modalclosers = document.querySelectorAll('.modal-close');
var shadaw = document.querySelector('.full-shadaw');

sidebarbuttons.forEach(function (btn, i, nodes) {
    btn.addEventListener('click', function (e) {
        e.preventDefault();
        if (btn.hasAttribute('data-id')) {
            let id = btn.getAttribute('data-id');
            let sbar = document.getElementById(id);
            if (sbar.classList.contains('sidebar-menu')) {
                sbar.classList.add('sidebar-menu-active');
            }
        }
    });
});

modalbuttons.forEach(function (btn, i, nodes) {
    btn.addEventListener('click', function (e) {
        e.preventDefault();
        if (btn.hasAttribute('data-id')) {
            let id = btn.getAttribute('data-id');
            let modal = document.getElementById(id);
            if (modal.classList.contains('modal')) {
                shadaw.classList.add('full-shadaw-show');
                modal.classList.add('modal-show');
            }
        }
    });
});


function hideAll() {
    let modals = document.querySelectorAll('.modal-show');
    let sidebars = document.querySelectorAll('.sidebar-menu-active');
    for (modal of modals) {
        modal.classList.remove('modal-show');
    }
    for (sidebar of sidebars) {
        sidebar.classList.remove('sidebar-menu-active');
    }
    shadaw.classList.remove('full-shadaw-show');
}
shadaw.addEventListener('click', function (evnt) {
    evnt.preventDefault();
    hideAll();
});
window.addEventListener("keydown", function (evt) {
    if (evt.keyCode === 27) {
        evt.preventDefault();
        hideAll();
    }
});
menuclosers.forEach(function (closer, i, nodes) {
    closer.addEventListener('click', function (evnt) {
        evnt.preventDefault();
        hideAll();
    });
});

modalclosers.forEach(function (closer, i, nodes) {
    closer.addEventListener('click', function (evnt) {
        evnt.preventDefault();
        hideAll();
    });
});