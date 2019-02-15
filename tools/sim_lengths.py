import sys
sys.path.insert(0, '../reports/code_blocks')
import ref_help as mv

def get_lgts(head, tail, sol, forcefield):
    if forcefield == 'martini':
        nc3 = {'N': 1, 'C': 5, head: 13}
        po4 = {'P': 1, 'O': 4}
        gl1 = {'C': 2, 'O': 2, tail: 2}
        gl2 = {'C': 3, 'O': 2, tail: 3}
        c1a = {'C': 5, tail: 10}
        c2a = {'C': 4, tail: 8}
        c3a = {'C': 4, tail: 8}
        c4a = {'C': 4, tail: 9}
        c1b = {'C': 5, tail: 10}
        c2b = {'C': 4, tail: 8}
        c3b = {'C': 4, tail: 8}
        c4b = {'C': 4, tail: 9}
        w = {'O': 2, sol: 4}
        wp = {'O': 1, sol: 2}
        wm = {'O': 1, sol: 2}
        scat_lens = []
        types = [nc3, po4, gl1, gl2, c1a, c2a, c3a, c4a, c1b, c2b, c3b, c4b]
        types_strings = ['NC3', 'PO4', 'GL1', 'GL2', 'C1A', 'C2A', 'C3A', 'C4A', 'C1B', 'C2B', 'C3B', 'C4B', 'W', 'WP', 'WM']
        for atom in types:
            comp = (mv.get_scattering_length(atom, neutron=True))
            scat_lens.append([comp.real, comp.imag])
        if sol == 'acmw':
            scat_lens.append([0, 0])
            scat_lens.append([0, 0])
            scat_lens.append([0, 0])
        else:
            types = [w, wp, wm]
            for atom in types:
                comp = (mv.get_scattering_length(atom, neutron=True))
                scat_lens.append([comp.real, comp.imag])
    elif forcefield == 'berger':
        c1 = {'C': 1, head: 3}
        c2 = {'C': 1, head: 3}
        c3 = {'C': 1, head: 3}
        n4 = {'N': 1}
        c5 = {'C': 1, head: 2}
        c6 = {'C': 1, head: 2}
        o7 = {'O': 1}
        p8 = {'P': 1}
        o9 = {'O': 1}
        o10 = {'O': 1}
        o11 = {'O': 1}
        c12 = {'C': 1, tail: 2}
        c13 = {'C': 1, tail: 1}
        o14 = {'O': 1}
        c15 = {'C': 1}
        o16 = {'O': 1}
        c17 = {'C': 1, tail: 2}
        c18 = {'C': 1, tail: 2}
        c19 = {'C': 1, tail: 2}
        c20 = {'C': 1, tail: 2}
        c21 = {'C': 1, tail: 2}
        c22 = {'C': 1, tail: 2}
        c23 = {'C': 1, tail: 2}
        c24 = {'C': 1, tail: 2}
        c25 = {'C': 1, tail: 2}
        c26 = {'C': 1, tail: 2}
        c27 = {'C': 1, tail: 2}
        c28 = {'C': 1, tail: 2}
        c29 = {'C': 1, tail: 2}
        c30 = {'C': 1, tail: 2}
        c31 = {'C': 1, tail: 2}
        c32 = {'C': 1, tail: 2}
        c33 = {'C': 1, tail: 3}
        c34 = {'C': 1, tail: 2}
        o35 = {'O': 1}
        c36 = {'C': 1}
        o37 = {'O': 1}
        c38 = {'C': 1, tail: 2}
        c39 = {'C': 1, tail: 2}
        c40 = {'C': 1, tail: 2}
        c41 = {'C': 1, tail: 2}
        c42 = {'C': 1, tail: 2}
        c43 = {'C': 1, tail: 2}
        c44 = {'C': 1, tail: 2}
        c45 = {'C': 1, tail: 2}
        c46 = {'C': 1, tail: 2}
        c47 = {'C': 1, tail: 2}
        c48 = {'C': 1, tail: 2}
        c49 = {'C': 1, tail: 2}
        c50 = {'C': 1, tail: 2}
        c51 = {'C': 1, tail: 2}
        c52 = {'C': 1, tail: 2}
        c53 = {'C': 1, tail: 2}
        c54 = {'C': 1, tail: 3}
        ow = {'O': 1}
        hw1 = {sol: 1}
        hw2 = {sol: 1}
        scat_lens = []
        types = [c1, c2, c3, n4, c5, c6, o7, p8, o9, o10, o11, c12, c13, o14, c15, o16, c17, c18, c19,
                 c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30, c31, c32, c33, c34, o35, c36,
                 o37, c38, c39, c40, c41, c42, c43, c44, c45, c46, c47, c48, c49, c50, c51, c52, c53, c54]
        types_strings = ['C1', 'C2', 'C3', 'N4', 'C5', 'C6', 'O7', 'P8', 'O9', 'O10', 'O11', 'C12', 'C13',
                         'O14', 'C15', 'O16', 'C17', 'C18', 'C19', 'C20', 'C21', 'C22', 'C23', 'C24',
                         'C25', 'C26', 'C27', 'C28', 'C29', 'C30', 'C31', 'C32', 'C33', 'C34', 'O35',
                         'C36', 'O37', 'C38', 'C39', 'C40', 'C41', 'C42', 'C43', 'C44', 'C45', 'C46',
                         'C47', 'C48', 'C49', 'C50', 'C51', 'C52', 'C53', 'C54', 'OW', 'HW1', 'HW2']
        for atom in types:
            comp = (mv.get_scattering_length(atom, neutron=True))
            scat_lens.append([comp.real, comp.imag])
        if sol == 'acmw':
            scat_lens.append([0, 0])
            scat_lens.append([0, 0])
            scat_lens.append([0, 0])
        else:
            types = [ow, hw1, hw2]
            for atom in types:
                comp = (mv.get_scattering_length(atom, neutron=True))
                scat_lens.append([comp.real, comp.imag])
    elif forcefield == 'slipids':
        n = {'N': 1}
        c13 = {'C': 1}
        h13a = {head: 1}
        h13b = {head: 1}
        h13c = {head: 1}
        c14 = {'C': 1}
        h14a = {head: 1}
        h14b = {head: 1}
        h14c = {head: 1}
        c15 = {'C': 1}
        h15a = {head: 1}
        h15b = {head: 1}
        h15c = {head: 1}
        c12 = {'C': 1}
        h12a = {head: 1}
        h12b = {head: 1}
        c11 = {'C': 1}
        h11a = {head: 1}
        h11b = {head: 1}
        p = {'P': 1}
        o13 = {'O': 1}
        o14 = {'O': 1}
        o11 = {'O': 1}
        o12 = {'O': 1}
        c1 = {'C': 1}
        ha = {tail: 1}
        hb = {tail: 1}
        c2 = {'C': 1}
        hs = {tail: 1}
        o21 = {'O': 1}
        c21 = {'C': 1}
        o22 = {'O': 1}
        c22 = {'C': 1}
        h2r = {tail: 1}
        h2s = {tail: 1}
        c3 = {'C': 1}
        hx = {tail: 1}
        hy = {tail: 1}
        o31 = {'O': 1}
        c31 = {'C': 1}
        o32 = {'O': 1}
        c32 = {'C': 1}
        h2x = {tail: 1}
        h2y = {tail: 1}
        c23 = {'C': 1}
        h3r = {tail: 1}
        h3s = {tail: 1}
        c24 = {'C': 1}
        h4r = {tail: 1}
        h4s = {tail: 1}
        c25 = {'C': 1}
        h5r = {tail: 1}
        h5s = {tail: 1}
        c26 = {'C': 1}
        h6r = {tail: 1}
        h6s = {tail: 1}
        c27 = {'C': 1}
        h7r = {tail: 1}
        h7s = {tail: 1}
        c28 = {'C': 1}
        h8r = {tail: 1}
        h8s = {tail: 1}
        c29 = {'C': 1}
        h9r = {tail: 1}
        h9s = {tail: 1}
        c210 = {'C': 1}
        h10r = {tail: 1}
        h10s = {tail: 1}
        c211 = {'C': 1}
        h11r = {tail: 1}
        h11s = {tail: 1}
        c212 = {'C': 1}
        h12r = {tail: 1}
        h12s = {tail: 1}
        c213 = {'C': 1}
        h13r = {tail: 1}
        h13s = {tail: 1}
        c214 = {'C': 1}
        h14r = {tail: 1}
        h14s = {tail: 1}
        c215 = {'C': 1}
        h15r = {tail: 1}
        h15s = {tail: 1}
        c216 = {'C': 1}
        h16r = {tail: 1}
        h16s = {tail: 1}
        c217 = {'C': 1}
        h17r = {tail: 1}
        h17s = {tail: 1}
        c218 = {'C': 1}
        h18r = {tail: 1}
        h18s = {tail: 1}
        h18t = {tail: 1}
        c33 = {'C': 1}
        h3x = {tail: 1}
        h3y = {tail: 1}
        c34 = {'C': 1}
        h4x = {tail: 1}
        h4y = {tail: 1}
        c35 = {'C': 1}
        h5x = {tail: 1}
        h5y = {tail: 1}
        c36 = {'C': 1}
        h6x = {tail: 1}
        h6y = {tail: 1}
        c37 = {'C': 1}
        h7x = {tail: 1}
        h7y = {tail: 1}
        c38 = {'C': 1}
        h8x = {tail: 1}
        h8y = {tail: 1}
        c39 = {'C': 1}
        h9x = {tail: 1}
        h9y = {tail: 1}
        c310 = {'C': 1}
        h10x = {tail: 1}
        h10y = {tail: 1}
        c311 = {'C': 1}
        h11x = {tail: 1}
        h11y = {tail: 1}
        c312 = {'C': 1}
        h12x = {tail: 1}
        h12y = {tail: 1}
        c313 = {'C': 1}
        h13x = {tail: 1}
        h13y = {tail: 1}
        c314 = {'C': 1}
        h14x = {tail: 1}
        h14y = {tail: 1}
        c315 = {'C': 1}
        h15x = {tail: 1}
        h15y = {tail: 1}
        c316 = {'C': 1}
        h16x = {tail: 1}
        h16y = {tail: 1}
        c317 = {'C': 1}
        h17x = {tail: 1}
        h17y = {tail: 1}
        c318 = {'C': 1}
        h18x = {tail: 1}
        h18y = {tail: 1}
        h18z = {tail: 1}
        ow = {'O': 1}
        hw1 = {sol: 1}
        hw2 = {sol: 1}
        scat_lens = []
        types = [n, c13, h13a, h13b, h13c, c14, h14a, h14b, h14c, c15, h15a, h15b, h15c, c12, h12a, h12b,
                 c11, h11a, h11b, p, o13, o14, o11, o12, c1, ha, hb, c2, hs, o21, c21, o22, c22, h2r, h2s,
                 c3, hx, hy, o31, c31, o32, c32, h2x, h2y, c23, h3r, h3s, c24, h4r, h4s, c25, h5r, h5s, c26,
                 h6r, h6s, c27, h7r, h7s, c28, h8r, h8s, c29, h9r, h9s, c210, h10r, h10s, c211, h11r, h11s,
                 c212, h12r, h12s, c213, h13r, h13s, c214, h14r, h14s, c215, h15r, h15s, c216, h16r, h16s,
                 c217, h17r, h17s, c218, h18r, h18s, h18t, c33, h3x, h3y, c34, h4x, h4y, c35, h5x, h5y, c36,
                 h6x, h6y, c37, h7x, h7y, c38, h8x, h8y, c39, h9x, h9y, c310, h10x, h10y, c311, h11x, h11y,
                 c312, h12x, h12y, c313, h13x, h13y, c314, h14x, h14y, c315, h15x, h15y, c316, h16x, h16y,
                 c317, h17x, h17y, c318, h18x, h18y, h18z]
        types_strings = ['N', 'C13', 'H13A', 'H13B', 'H13C', 'C14', 'H14A', 'H14B', 'H14C', 'C15', 'H15A',
                         'H15B', 'H15C', 'C12', 'H12A', 'H12B', 'C11', 'H11A', 'H11B', 'P', 'O13', 'O14',
                         'O11', 'O12', 'C1', 'HA', 'HB', 'C2', 'HS', 'O21', 'C21', 'O22', 'C22', 'H2R',
                         'H2S', 'C3', 'HX', 'HY', 'O31', 'C31', 'O32', 'C32', 'H2X', 'H2Y', 'C23', 'H3R',
                         'H3S', 'C24', 'H4R', 'H4S', 'C25', 'H5R', 'H5S', 'C26', 'H6R', 'H6S', 'C27', 'H7R',
                         'H7S', 'C28', 'H8R', 'H8S', 'C29', 'H9R', 'H9S', '0C21', 'H10R', 'H10S', '1C21',
                         'H11R', 'H11S', '2C21', 'H12R', 'H12S', '3C21', 'H13R', 'H13S', '4C21', 'H14R',
                         'H14S', '5C21', 'H15R', 'H15S', '6C21', 'H16R', 'H16S', '7C21', 'H17R', 'H17S',
                         '8C21', 'H18R', 'H18S', 'H18T', 'C33', 'H3X', 'H3Y', 'C34', 'H4X', 'H4Y', 'C35',
                         'H5X', 'H5Y', 'C36', 'H6X', 'H6Y', 'C37', 'H7X', 'H7Y', 'C38', 'H8X', 'H8Y',
                         'C39', 'H9X', 'H9Y', '0C31', 'H10X', 'H10Y', '1C31', 'H11X', 'H11Y', '2C31',
                         'H12X', 'H12Y', '3C31', 'H13X', 'H13Y', '4C31', 'H14X', 'H14Y', '5C31', 'H15X',
                         'H15Y', '6C31', 'H16X', 'H16Y', '7C31', 'H17X', 'H17Y', '8C31', 'H18X', 'H18Y', 'H18Z',
                         'OW', 'HW1', 'HW2']
        for i, atom in enumerate(types):
            comp = (mv.get_scattering_length(atom, neutron=True))
            scat_lens.append([comp.real, comp.imag])
        if sol == 'acmw':
            scat_lens.append([0, 0])
            scat_lens.append([0, 0])
            scat_lens.append([0, 0])
        else:
            types = [ow, hw1, hw2]
            for atom in types:
                comp = (mv.get_scattering_length(atom, neutron=True))
                scat_lens.append([comp.real, comp.imag])
    return [types_strings, scat_lens]
