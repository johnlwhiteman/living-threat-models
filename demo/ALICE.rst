Living THREATS.md
#################

Install Alice https://github.com/pdxjohnny/dffml/tree/manifest/entities/alice

Create the ``THREATS.md`` file

.. code-block:: console

    $ alice threats \
        -inputs \
          models/good.json=ThreatDragonThreatModelPath \
          models/GOOD_THREATS.md=ThreatsMdPath

We made ``auditor_overlay.py`` which is a data flow which calls the auditor. We
use ``sed`` to direct the data flow to run on the path to the threat model from
Threat Dragon used as input.

.. code-block:: console

    $ dffml service dev export auditor_overlay:AUDITOR_OVERLAY \
        -configloader yaml \
        | sed -e 's/auditor_overlay:audit.inputs.ltm/ThreatDragonThreatModelPath/g' \
        | tee auditor_overlay.yaml

Generate ``GOOD_THREATS.md`` with auditing overlay.

.. code-block:: console

    $ alice threats -log debug \
        -overlay auditor_overlay.yaml \
        -inputs \
          models/good.json=ThreatDragonThreatModelPath \
          models/GOOD_THREATS.md=ThreatsMdPath

Generate ``BAD_THREATS.md`` with auditing overlay.

.. code-block:: console

    $ alice threats -log debug \
        -overlay auditor_overlay.yaml \
        -inputs \
          models/bad.json=ThreatDragonThreatModelPath \
          models/BAD_THREATS.md=ThreatsMdPath

Dump out to HTTP to copy to GitHub for rendering.

.. code-block:: console

    $ (echo -e 'HTTP/1.0 200 OK\n' && cat models/GOOD_THREATS.md) | nc -Nlp 9999;
    $ (echo -e 'HTTP/1.0 200 OK\n' && cat models/BAD_THREATS.md) | nc -Nlp 9999;
