#!/usr/bin/env python3
"""
Unit test verifying parity_auditor package execution entry point (__main__.py).
"""

import os
import subprocess
import sys
import unittest

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PARITY_SRC = os.path.join(PROJECT_ROOT, "skills", "spec-orchestrator", "parity_auditor", "src")


class TestParityAuditorMain(unittest.TestCase):
    """Verifies that `python3 -m parity_auditor` executes cleanly without ModuleNotFoundError."""

    def test_parity_auditor_module_execution_help(self):
        env = os.environ.copy()
        env["PYTHONPATH"] = PARITY_SRC + (os.pathsep + env["PYTHONPATH"] if "PYTHONPATH" in env else "")

        res = subprocess.run(
            [sys.executable, "-m", "parity_auditor", "--help"],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            env=env,
        )
        self.assertEqual(res.returncode, 0, f"Command failed with stderr: {res.stderr}")
        self.assertIn("Model Coverage Parity Audit CLI", res.stdout)
        self.assertNotIn("No module named parity_auditor.__main__", res.stderr)


if __name__ == "__main__":
    unittest.main()
