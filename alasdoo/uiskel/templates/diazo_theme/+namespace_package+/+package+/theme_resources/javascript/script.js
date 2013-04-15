;(function ($) {
    $(function () {

        //
        // Main menu affix
        // ------------------------------------------------------

        // Fix the main menu to the top when scrolled down.
        var offsetTop = $('.navbar-inner').offset().top;
        $('.navbar').affix({offset: offsetTop});


        //
        // MOBILE MENU AND SEARCH
        // ------------------------------------------------------

        var $menu = $('.navbar'),
            $menuBtn = $('#mobile-globalnav'),
            $search = $('#portal-searchbox'),
            $searchBtn = $('#mobile-search'),
            $quicklinks = $('#quicklinks');

        $menuBtn.bind('click', function() {
            // mark the button as active
            $menuBtn.toggleClass('active');
            $searchBtn.removeClass('active');

            // toggle menu and search
            $menu.toggleClass('visible');
            $search.removeClass('visible');

            // show quicklinks only when the menu is closed
            $quicklinks.toggle(!$menu.hasClass('visible'));
        });

        $searchBtn.bind('click', function() {
            // mark the button as active
            $menuBtn.removeClass('active');
            $searchBtn.toggleClass('active');

            // toggle menu and search
            $search.toggleClass('visible');
            $menu.removeClass('visible');

            // show quicklinks only when the search is closed
            $quicklinks.toggle(!$search.hasClass('visible'));
        });

        $('#mobile-page-settings').bind('click', function() {
            $('#edit-bar').toggleClass('visible');
            $(this).toggleClass('selected');
        });

    });
}(jQuery));
