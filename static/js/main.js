var sidebarbuttons = document.querySelectorAll('[data-cmd="sidebarbutton"]');
var modalbuttons = document.querySelectorAll('[data-cmd="modalbutton"]');
var menuclosers = document.querySelectorAll('.close-button');
var modalclosers = document.querySelectorAll('.modal-close');
var shadaw = document.querySelector('.full-shadaw');
var menutitles = document.querySelectorAll('.menu-title');
var menulists = document.querySelectorAll('.menu-list');

function hideAll() {
    let modals = document.querySelectorAll('.modal-show');
    let sidebars = document.querySelectorAll('.sidebar-menu-active');
    modals.forEach(function (modal, i, node) {
        modal.classList.remove('modal-show');
    });
    sidebars.forEach(function (sidebar, i, node) {
        sidebar.classList.remove('sidebar-menu-active');
    });
    shadaw.classList.remove('full-shadaw-show');
}

menutitles.forEach(function (menu, i, node) {
    menu.addEventListener('click', function (evnt) {
        evnt.preventDefault();
        menu.parentElement.classList.toggle('menu-opened');
    });
});
sidebarbuttons.forEach(function (btn, i, nodes) {
    btn.addEventListener('click', function (e) {
        e.preventDefault();
        if (btn.hasAttribute('data-id')) {
            let id = btn.getAttribute('data-id');
            let sbar = document.getElementById(id);
            if (sbar.classList.contains('sidebar-menu')) {
                hideAll();
                sbar.classList.add('sidebar-menu-active');
                sbar.scrollIntoView();
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
menulists.forEach(function (item, i, node) {
    if (item.childElementCount == 0) {
        item.parentElement.style.display = 'none';
    }
})