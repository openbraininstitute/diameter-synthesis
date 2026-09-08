"""Tests for the diameter_synthesis.utils module."""

# Copyright (C) 2021-2024  Blue Brain Project, EPFL
#
# SPDX-License-Identifier: Apache-2.0

from diameter_synthesis import utils


def test_create_morphologies_dict_xml_skips_invalid_entries(tmp_path):
    """Invalid morphology entries are skipped without failing the whole parse."""
    morph_dir = tmp_path / "morphs"
    morph_dir.mkdir()
    (morph_dir / "neuronDB.xml").write_text(
        """<?xml version="1.0"?>
        <root>
          <listing>
            <morphology>
              <mtype>L5</mtype>
              <msubtype></msubtype>
              <name>valid</name>
            </morphology>
            <morphology>
              <name>invalid.asc</name>
            </morphology>
          </listing>
        </root>
        """,
        encoding="utf-8",
    )

    result = utils._create_morphologies_dict_xml(f"{morph_dir}/", "neuronDB.xml")

    assert result == {"L5": ["valid.asc"]}
