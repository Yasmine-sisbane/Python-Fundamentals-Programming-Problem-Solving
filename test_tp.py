import contextlib
import io
import builtins
import unittest
from pathlib import Path
import nbformat

NB_PATH = Path(__file__).resolve().parents[1] / "TP1python_partie1_corrige.ipynb"
NB = nbformat.read(NB_PATH, as_version=4)
CELLS = {c.metadata["exercice"]: c.source for c in NB.cells
         if c.cell_type == "code" and "exercice" in c.metadata}

def eval_cell(num, values=()):
    answers = iter(map(str, values))
    stdout = io.StringIO()
    orig_input = builtins.input
    def next_input(prompt=''):
        x = next(answers)
        print(str(prompt) + x)
        return x
    try:
        builtins.input = next_input
        with contextlib.redirect_stdout(stdout):
            exec(CELLS[num], {})
    finally:
        builtins.input = orig_input
    return stdout.getvalue()

class TestTP1(unittest.TestCase):
    def test_01_moyenne_ponderee(self):
        self.assertIn("14.8 / 20", eval_cell(1, ['CNE123456',16,14,2,3]))

    def test_02_somme_coefficients_nulle(self):
        self.assertIn("somme des coefficients", eval_cell(1,['ETU',12,10,0,0]))

    def test_03_deux_solutions(self):
        out=eval_cell(2,[1,-3,2])
        self.assertIn('Deux solutions',out)
        self.assertIn('x1 = 1.0',out)

    def test_04_racine_double(self):
        self.assertIn('solution réelle double',eval_cell(2,[1,-2,1]))

    def test_05_aucune_solution_reelle(self):
        self.assertIn('Aucune solution réelle',eval_cell(2,[1,0,1]))

    def test_06_equation_lineaire(self):
        self.assertIn('premier degré',eval_cell(2,[0,2,4]))

    def test_07_equation_indeterminee(self):
        self.assertIn('tous les réels',eval_cell(2,[0,0,0]))

    def test_08_equation_impossible(self):
        self.assertIn('aucune solution',eval_cell(2,[0,0,5]))

    def test_09_validation_impair(self):
        out=eval_cell(3,[4,'3.5',5])
        self.assertIn('nombre pair',out)
        self.assertIn('saisie non entière',out)
        self.assertRegex(out, r'(?m)^5$')

    def test_10_impair_negatif(self):
        out=eval_cell(3,[-3])
        self.assertRegex(out,r'(?m)^-3$')

    def test_11_saisie_invalide(self):
        self.assertIn('saisie non entière',eval_cell(3,['abc',1]))

    def test_12_bonification(self):
        out=eval_cell(4)
        self.assertIn('Valeur initiale de x : 10',out)
        self.assertIn('14.0',out)
        self.assertIn('17.5',out)

    def test_13_mediane_impaire_avec_rejet(self):
        out=eval_cell(5,[5,10,9,12,14,16,18])
        self.assertIn('ordre croissant',out)
        self.assertIn('Médiane : 14.0',out)

    def test_14_mediane_paire(self):
        self.assertIn('Médiane : 12.5',eval_cell(5,[4,10,12,13,18]))

    def test_15_nb_notes_incorrect(self):
        self.assertIn('strictement positif',eval_cell(5,[0,1,15]))

    def test_16_agent_calculatrice(self):
        self.assertEqual('Calculatrice',eval_cell(6).strip())

if __name__ == '__main__':
    unittest.main()
