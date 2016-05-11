Geofront
========

.. image:: https://badges.gitter.im/spoqa/geofront.svg
   :alt: Join the chat at https://gitter.im/spoqa/geofront
   :target: https://gitter.im/spoqa/geofront?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

.. image:: https://badge.fury.io/py/Geofront.svg?
   :target: https://pypi.python.org/pypi/Geofront
   :alt: Latest PyPI version

.. image:: https://readthedocs.org/projects/geofront/badge/
   :target: https://geofront.readthedocs.org/
   :alt: Read the Docs

.. image:: https://travis-ci.org/spoqa/geofront.svg?branch=master
   :target: https://travis-ci.org/spoqa/geofront

.. image:: https://img.shields.io/coveralls/spoqa/geofront.svg
   :target: https://coveralls.io/r/spoqa/geofront

Geofront is a simple SSH key management server.  It helps to maintain servers
to SSH, and ``authorized_keys`` list for them.  `Read the docs`__ for more
details.

__ https://geofront.readthedocs.org/


Situations
----------

- If the team maintains ``authorized_keys`` list of all servers owned
  by the team:

  - When someone joins or leaves the team, all lists have to be updated.
  - *Who* do update the list?

- If the team maintains shared private keys to SSH servers:

  - These keys have to be expired when someone leaves the team.
  - There should be a shared storage for the keys.  (Dropbox?  srsly?)
  - Everyone might need to add ``-i`` option to use team's own key.

- The above ways are both hard to scale servers.  Imagine your team
  has more than 10 servers.


Idea
----

1. Geofront has its own *master key*.  The private key is never shared.
   The master key is periodically and automatically regened.
2. Every server has a simple ``authorized_keys`` list, which authorizes
   only the master key.
3. Every member registers their own public key to Geofront.
   The registration can be omitted if the key storage is GitHub, Bitbucket,
   etc.
4. A member requests to SSH a server, then Geofront *temporarily*
   (about 30 seconds, or a minute) adds their public key to ``authorized_keys``
   of the requested server.

GitHub/Docker Quick Setup
-------------------------

Server

example ``geofront.cfg.py``

.. code:: python

   # GitHub Org
   from geofront.backends.github import GitHubOrganization
   
   TEAM = GitHubOrganization(
      client_id='id',
      client_secret='secret',
      org_login='org'
   )
   
   # GitHub Key Store
   from geofront.backends.github import GitHubKeyStore
   KEY_STORE = GitHubKeyStore()
   
   # Master key store
   from geofront.masterkey import FileSystemMasterKeyStore
   MASTER_KEY_STORE = FileSystemMasterKeyStore('/config/master_key')
   
   # Redis Cache
   from werkzeug.contrib.cache import RedisCache
   TOKEN_STORE = RedisCache(host='localhost', db=0)
   
   # Servers
   from geofront.remote import Remote
   REMOTE_SET = {
     'servername': Remote('user', 'host')
   }

1. Setup OAuth App in Github Org, with callback URL set to the IP or domain of the geofront server, add the client id and secret to the geofront config
2. Set the ``REMOTE_SET`` in the config to the servers you want to connect to
3. Set the redis host in config to point to a redis server
4. Set the master key store config e.g. ``/config/master_key``
5. ``docker run -d -p 80:8080 -v /path/to/config:/config --name geofront sett/geofront`` or choose some other port and reverse proxy nginx to it. Link redis if using a locally e.g. ``--link redis:redis``

Client

1. Install python3 with pip
2. If you're on windows install pywin32: https://sourceforge.net/projects/pywin32/files/pywin32/Build%20220/
3. ``pip install geofront-cli``
4. ``geofront-cli start`` - enter URL of geofront server
5. ``geofront-cli remotes`` - should create a list of servers
6. ``geofront-cli colonize <remote>`` - you need access to the remote with your local key - this will add geofronts key to the remote server
7. ``geofront-cli ssh <remote>`` - should now work (but not on windows)


Prerequisites
-------------

- Linux, BSD, Mac
- Python 3.3+
- Third-party packages (automatically installed together)

  - Paramiko_ 1.13.0+
  - Werkzeug_ 0.9+
  - Flask_ 0.10+
  - OAuthLib_ 1.0.3+
  - Apache Libcloud_ 0.15.0+
  - Waitress_ 0.8.8+
  - singledispatch_ (only if Python is older than 3.4)

.. _Paramiko: http://www.paramiko.org/
.. _Werkzeug: http://werkzeug.pocoo.org/
.. _Flask: http://flask.pocoo.org/
.. _OAuthLib: https://github.com/idan/oauthlib
.. _Libcloud: http://libcloud.apache.org/
.. _Waitress: https://github.com/Pylons/waitress
.. _singledispatch: https://pypi.python.org/pypi/singledispatch


Author and license
------------------

Geofront is written by `Hong Minhee`__, maintained by Spoqa_, and licensed
under AGPL3_ or later.  You can find the source code from GitHub__:

.. code-block:: console

   $ git clone git://github.com/spoqa/geofront.git


__ http://dahlia.kr/
.. _Spoqa: http://www.spoqa.com/
.. _AGPL3: http://www.gnu.org/licenses/agpl-3.0.html
__ https://github.com/spoqa/geofront


Missing features
----------------

- Google Apps backend [`#3`_]
- Bitbucket backend [`#4`_]
- Fabric_ integration
- PuTTY_ integration

(Contributions would be appreciated!)

.. _Fabric: http://www.fabfile.org/
.. _PuTTY: http://www.chiark.greenend.org.uk/~sgtatham/putty/
.. _#3: https://github.com/spoqa/geofront/issues/3
.. _#4: https://github.com/spoqa/geofront/issues/4
