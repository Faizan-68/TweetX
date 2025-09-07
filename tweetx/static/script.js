(function() {
    var body = document.body;
    var toggle = document.querySelector('.menu-toggle');
    var sidebar = document.getElementById('sidebar');
    var backdrop = document.querySelector('.sidebar-backdrop');
    if (!toggle || !sidebar || !backdrop) return;

    function openSidebar() {
      body.classList.add('sidebar-open');
      toggle.setAttribute('aria-expanded', 'true');
    }
    function closeSidebar() {
      body.classList.remove('sidebar-open');
      toggle.setAttribute('aria-expanded', 'false');
    }
    function toggleSidebar() {
      if (body.classList.contains('sidebar-open')) {
        closeSidebar();
      } else {
        openSidebar();
      }
    }

    toggle.addEventListener('click', toggleSidebar);
    backdrop.addEventListener('click', closeSidebar);
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') {
        closeSidebar();
      }
    });

    // Close after clicking a link on mobile
    sidebar.addEventListener('click', function(e) {
      var target = e.target.closest('a');
      if (target && window.matchMedia('(max-width: 992px)').matches) {
        closeSidebar();
      }
    });
  })();