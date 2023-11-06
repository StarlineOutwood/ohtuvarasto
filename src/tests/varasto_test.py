import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.varasto_saldo = Varasto(10, 5)
        self.varasto_neg_saldo = Varasto(10, -5)
        self.varasto_liikaa_saldoa = Varasto(10, 20)
        self.varasto_neg_tilavuus = Varasto(-10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_uudella_varastolla_on_oikea_saldo(self):
        self.assertAlmostEqual(self.varasto_saldo.saldo, 5)

    def test_uudella_varastolla_ei_neg_saldo(self):
        self.assertAlmostEqual(self.varasto_neg_saldo.saldo, 0)

    def test_uudella_varastolla_ei_liikaa_saldoa(self):
        self.assertAlmostEqual(self.varasto_liikaa_saldoa.saldo, 10)

    def test_uudella_varastolla_ei_neg_tilavuus(self):
        self.assertAlmostEqual(self.varasto_neg_tilavuus.tilavuus, 0)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_ei_voi_lisata_yli_tilavuuden(self):
        self.varasto.lisaa_varastoon(14)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ei_voi_lisata_negatiivista(self):
        self.varasto.lisaa_varastoon(-4)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_osaa_kertoa_paljon_mahtuu(self):
        self.varasto.lisaa_varastoon(4)
        self.assertEqual(self.varasto.paljonko_mahtuu(), 6)

    def test_ottaminen_vahentaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(4)

        self.assertAlmostEqual(self.varasto.saldo, 4)

    def test_osaa_ottaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ei_voi_ottaa_alle_nollan(self):
        self.varasto.lisaa_varastoon(4)
        self.varasto.ota_varastosta(5)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_ei_voi_ottaa_negatiivista(self):
        maara = self.varasto.ota_varastosta(-5)
        self.assertAlmostEqual(maara, 1)
