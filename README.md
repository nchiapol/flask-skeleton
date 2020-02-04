Flask Skeleton
==============

Repo with a minimal Flask-skeleton to speed up the start of projects.

Things to adjust
----------------
- change `myname` to something useful (folder + `grep -r myname *`)
- change `myblue` to something useful (`myname/myblue.py`, `myname/templates/myblue/`, `grep -r myblue *`)
- adapt `schema.sql` and create database `cd instance; sqlite3 data.db < ../myname/schema.sql`
- adapt Blueprint (in the former `myblue.py`)


Pointers
--------
You might also want to look at https://github.com/pallets/flask/tree/master/examples/tutorial for a similar base.

