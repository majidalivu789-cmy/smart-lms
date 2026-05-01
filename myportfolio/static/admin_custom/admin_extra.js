document.addEventListener('DOMContentLoaded', function () {
    const instructorLink = Array.from(document.querySelectorAll('#jazzy-navbar .nav-link')).find(function (link) {
        return link.textContent.trim() === 'Instructor';
    });

    if (!instructorLink) {
        return;
    }

    const navItem = instructorLink.closest('.nav-item');
    if (!navItem) {
        return;
    }

    navItem.classList.add('dropdown');
    instructorLink.classList.add('dropdown-toggle');
    instructorLink.setAttribute('href', '#');
    instructorLink.setAttribute('role', 'button');
    instructorLink.setAttribute('data-bs-toggle', 'dropdown');
    instructorLink.setAttribute('data-instructor-menu', 'true');
    instructorLink.setAttribute('aria-haspopup', 'true');
    instructorLink.setAttribute('aria-expanded', 'false');

    const dropdown = document.createElement('div');
    dropdown.className = 'dropdown-menu';
    dropdown.innerHTML = [
        '<a class="dropdown-item" href="/admin/Home_Page/instructor/">Instructors</a>',
        '<a class="dropdown-item" href="/admin/Home_Page/instructordetail/">Instructor Details</a>',
        '<a class="dropdown-item" href="/admin/Home_Page/instructorcourse/">Instructor Courses</a>',
        '<a class="dropdown-item" href="/admin/Home_Page/instructorreview/">Instructor Reviews</a>'
    ].join('');

    navItem.appendChild(dropdown);

    const instructorUrls = [
        '/admin/Home_Page/instructordetail/',
        '/admin/Home_Page/instructorcourse/',
        '/admin/Home_Page/instructorreview/'
    ];

    document.querySelectorAll('#jazzy-navbar .nav-item.dropdown').forEach(function (item) {
        if (item === navItem) {
            return;
        }

        instructorUrls.forEach(function (url) {
            const duplicate = item.querySelector('.dropdown-item[href="' + url + '"]');
            if (duplicate) {
                duplicate.remove();
            }
        });
    });
});
