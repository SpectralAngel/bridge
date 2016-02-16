======
Bridge
======

Bridge is an app designed to mediate TurboAffiliate related data to django
based projects

Quick start
-----------

1. Add "bridge" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'bridge',
    ]

2. Include the polls URLconf in your project urls.py like this::

    url(r'^bridge/', include('bridge.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   view data (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/bridge/ to participate in the poll.
