Geofront
========

Geofront is a simple SSH key management server.  It helps to maintain servers
to SSH, and ``authorized_keys`` list for them.


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
  have more than 10 servers.


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


Author and license
------------------

Geofront is written by `Hong Minhee`__, maintained by Spoqa_, and licensed
under AGPL3 or later.


__ http://dahlia.kr/
.. _Spoqa: http://www.spoqa.com/