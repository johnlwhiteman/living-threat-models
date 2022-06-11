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

We do not yet include the output in THREATS.md. Do do that, merge the two
dataflows together and edit the inputs of the
``generate_threat_model_sections`` from ``entities/alice/alice/threats_md.py``.

References:

- https://intel.github.io/dffml/master/cli.html#merge
- https://intel.github.io/dffml/master/examples/dataflows.html#combining-operations

.. code-block:: console

    $ dffml service dev export alice.threats_md:THREATS_MD_DATAFLOW \
        -configloader json \
        | tee threats_md_dataflow.json

Merge the dataflows ahead of time

.. code-block:: console

    $ dffml dataflow merge \
        threats_md_dataflow.json \
        auditor_overlay.yaml \
        | tee auditor_output_in_threats_md.json

Run with merged dataflow

.. code-block:: console

    $ alice threats -log debug \
        -dataflow auditor_output_in_threats_md.json \
        -inputs \
          models/bad.json=ThreatDragonThreatModelPath \
          models/BAD_THREATS.md=ThreatsMdPath

Observe output in ``BAD_THREATS.md``

.. todo::

    We don't yet do this because you'll need to override the
    generate_threat_model_sections a different way because right now it uses all
    the inputs by name, but in the future you can just add another input to it
    and it would take it in order and combine with the rest.
