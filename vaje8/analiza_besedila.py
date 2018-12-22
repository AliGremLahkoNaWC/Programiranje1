# =============================================================================
# Analiza besedila
#
# Pri tej nalogi bomo analizirali nize, ki predstavljajo pravilno slovensko 
# oblikovane besede in stavke. Pri vseh podnaloge lahko predpostavite, da so 
# vhodni nizi `s` dobro oblikovani, tj. ne vsebujejo dveh zaporednih presledkov 
# oz. nepotrebnih presledkov ter prelomov vrstice na začetku ali na koncu.
# =====================================================================@017495=
# 1. podnaloga
# Sestavite funkcijo `stevilo_besed(niz)`, ki v podanem nizu prešteje
# število besed, pri čemer lahko predpostavite, da presledki stojijo
# **natanko pred vsako** (razen prvo) besedo v nizu.
# Primer:
# 
#     >>> stevilo_besed('Višje, hitreje, močneje!')
#     3
# =============================================================================
def stevilo_besed(niz):
    '''funkcija steje besede v nizu.'''
    if niz == '':
        return 0
    besede = 1
    for x in niz:
        if x == ' ':
            besede += 1
    return besede
# =====================================================================@017496=
# 2. podnaloga
# Sestavite funkcijo `koliko_samoglasnikov(niz)`, ki v podanem nizu prešteje 
# število samoglasnikov. Primer:
# 
#     >>> koliko_samoglasnikov('pomaranča')
#     4
# =============================================================================
def koliko_samoglasnikov(niz):
    '''funkcija presteje stevilo samoglasnikov v nizu.'''
    
    samo = 'aeiouAEIOU'
    stevilo = 0
    for x in niz:
        if x in samo:
            stevilo += 1
    return stevilo
# =====================================================================@017497=
# 3. podnaloga
# V Pythonu vrstice večvrstičnega niza ločujemo z znakom `'\n'`. Sestavite 
# funkcijo `vrstice(niz)`, ki sprejme večvrstični niz in vrne seznam, ki 
# vsebuje vse vrstice tega niza (v enakem vrstnem redu).
# Primer:
# 
#     >>> vrstice("Danes\n je lep\ndan.\n")
#     ['Danes', ' je lep', 'dan.', '']
# 
# _Opomba_: Python obravnava niz `'\n'` kot en sam znak.
# =============================================================================
def vrstice(niz):
    '''funkcija sestavi tabelo besed iz podanega niza. elemente loci,
    ce je v nizu \n.'''
    
    prazen_niz = ''
    tabela = []
    
    for x in niz:
        
        if x == '\n':
            tabela.append(prazen_niz)
            prazen_niz = ''
        else:
            prazen_niz = prazen_niz + x
    tabela.append(prazen_niz)
    return tabela
# =====================================================================@017498=
# 4. podnaloga
# Haiku (japonsko 俳句) je japonska pesniška oblika iz treh verzov (vrstic), ki 
# obsega sedemnajst zlogov. Prvi in tretji verz imata po pet zlogov, drugi 
# sedem.
# 
# Na kulturnem natečaju TomoHaiku udeleženci oddajajo svoje izdelke na strežnik
# Tomo. Napišite kontrolno funkcijo `je_haiku(niz)`, ki sprejme niz, ter vrne 
# `True`, če niz ustreza pesniški obliki haiku, sicer pa vrne `False`.
# 
# Predpostavite lahko, da število samoglasnikov v neki besedi ustreza številu 
# njenih zlogov, ter da niz ne vsebuje nepotrebnih začetnih oz. končnih praznih
# vrstic. Vrstice so ločene z znakom za prelom vrstice `'\n'`.
# Primer:
# 
#     >>> je_haiku('Skrit v svojem svetu,\ntemna otožnost neba,\ntvoj topli objem.')
#     True
#     >>> je_haiku('Riba,\nraca, rak,\nvinjak je grenak!')
#     False
# =============================================================================
def je_haiku(niz):
    '''funkcija ugotavlja ali je niz haiku.'''
    
    tabela = vrstice(niz)
    if len(tabela) == 1:
        return False
    elif koliko_samoglasnikov(tabela[0]) == koliko_samoglasnikov(tabela[2]) and koliko_samoglasnikov(tabela[1]) == 7:
        return True
    else:
        return False
        
# =====================================================================@017499=
# 5. podnaloga
# Sestavite funkcijo `podcrtaj(niz)`, ki za parameter dobi niz, v katerem so 
# podnizi, ki bi morali biti izpisani podčrtano, označeni s podčrtajem na 
# začetku in na koncu. Če je v nizu liho mnogo podčrtajev, si mislite, da je še 
# eden na koncu. Funkcija naj vrne dvovrstični niz, kjer je v prvi vrstici 
# izvorni niz toda brez podčrtajev, sledi znak za prelom vrstice, naslednjo 
# vrstico pa sestavlja niz, sestavljen iz presledkov in minusov, pri čemer 
# minusi ležijo pod tistimi deli besedila, ki morajo biti podčrtani.
# Primer:
# 
#     >>> podcrtaj("Jaz _sem_ pa cajzelc!")
#     'Jaz sem pa cajzelc!\n    ---            '
# 
# Predpostavite, da v nizu ni nobenega znaka `'\n'`.
# =============================================================================

# =====================================================================@017500=
# 6. podnaloga
# Sestavite funkcijo `stevilo_znakov(niz)`, ki v podanem nizu prešteje število
# znakov, pri čemer se presledki ne upoštevajo. 
# Primer:
# 
#     >>> stevilo_znakov('B     u!')
#     3
# =============================================================================

# =====================================================================@017501=
# 7. podnaloga
# [Sonet](https://sl.wikipedia.org/wiki/Sonet) je priljubljena pesniška oblika.
# Sestavljen je iz štirih kitic, pri čemur med vsakima dvema kiticama avtor 
# izpusti eno prazno vrstico. Prvi dve kitici sta štirivrstični — kvartini, 
# drugi dve pa sta trivrstični — tercini.
# 
# V slovenskem sonetu je standardni verz italijanski (laški) ali jambski
# enajsterec. To pomeni, da v vsaki vrstici nastopa natanko enajst zlogov.
# 
# Na kulturnem natečaju TomoSonet udeleženci oddajajo svoje izdelke na strežnik 
# Tomo. Napiši kontrolno funkcijo `je_sonet(niz)`, ki sprejme niz, ter vrne 
# `True`, če niz ustreza slovenskemu sonetu, in `False` sicer.
# Primer:
# 
#     >>> je_sonet('Bolj slab\nsonet.\n\nZa umret!')
#     False
# 
# _Namig_: V slovenskem jeziku število samoglasnikov v neki besedi ustreza
# številu njenih zlogov. (Obstaja nekaj izjem, ki pa jih bomo zanemarili.)
# =============================================================================





































































































# ============================================================================@

'Če vam Python sporoča, da je v tej vrstici sintaktična napaka,'
'se napaka v resnici skriva v zadnjih vrsticah vaše kode.'

'Kode od tu naprej NE SPREMINJAJTE!'


















































import json, os, re, sys, shutil, traceback, urllib.error, urllib.request


import io, sys
from contextlib import contextmanager

class VisibleStringIO(io.StringIO):
    def read(self, size=None):
        x = io.StringIO.read(self, size)
        print(x, end='')
        return x

    def readline(self, size=None):
        line = io.StringIO.readline(self, size)
        print(line, end='')
        return line

class Check:
    @staticmethod
    def has_solution(part):
        return part['solution'].strip() != ''

    @staticmethod
    def initialize(parts):
        Check.parts = parts
        for part in Check.parts:
            part['valid'] = True
            part['feedback'] = []
            part['secret'] = []
        Check.current_part = None
        Check.part_counter = None

    @staticmethod
    def part():
        if Check.part_counter is None:
            Check.part_counter = 0
        else:
            Check.part_counter += 1
        Check.current_part = Check.parts[Check.part_counter]
        return Check.has_solution(Check.current_part)

    @staticmethod
    def feedback(message, *args, **kwargs):
        Check.current_part['feedback'].append(message.format(*args, **kwargs))

    @staticmethod
    def error(message, *args, **kwargs):
        Check.current_part['valid'] = False
        Check.feedback(message, *args, **kwargs)

    @staticmethod
    def clean(x, digits=6, typed=False):
        t = type(x)
        if t is float:
            x = round(x, digits)
            # Since -0.0 differs from 0.0 even after rounding,
            # we change it to 0.0 abusing the fact it behaves as False.
            v = x if x else 0.0
        elif t is complex:
            v = complex(Check.clean(x.real, digits, typed), Check.clean(x.imag, digits, typed))
        elif t is list:
            v = list([Check.clean(y, digits, typed) for y in x])
        elif t is tuple:
            v = tuple([Check.clean(y, digits, typed) for y in x])
        elif t is dict:
            v = sorted([(Check.clean(k, digits, typed), Check.clean(v, digits, typed)) for (k, v) in x.items()])
        elif t is set:
            v = sorted([Check.clean(y, digits, typed) for y in x])
        else:
            v = x
        return (t, v) if typed else v

    @staticmethod
    def secret(x, hint=None, clean=None):
        clean = Check.get('clean', clean)
        Check.current_part['secret'].append((str(clean(x)), hint))

    @staticmethod
    def equal(expression, expected_result, clean=None, env=None, update_env=None):
        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get('clean', clean)
        actual_result = eval(expression, global_env)
        if clean(actual_result) != clean(expected_result):
            Check.error('Izraz {0} vrne {1!r} namesto {2!r}.',
                        expression, actual_result, expected_result)
            return False
        else:
            return True

    @staticmethod
    def run(statements, expected_state, clean=None, env=None, update_env=None):
        code = "\n".join(statements)
        statements = "  >>> " + "\n  >>> ".join(statements)
        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get('clean', clean)
        exec(code, global_env)
        errors = []
        for (x, v) in expected_state.items():
            if x not in global_env:
                errors.append('morajo nastaviti spremenljivko {0}, vendar je ne'.format(x))
            elif clean(global_env[x]) != clean(v):
                errors.append('nastavijo {0} na {1!r} namesto na {2!r}'.format(x, global_env[x], v))
        if errors:
            Check.error('Ukazi\n{0}\n{1}.', statements,  ";\n".join(errors))
            return False
        else:
            return True

    @staticmethod
    @contextmanager
    def in_file(filename, content, encoding=None):
        encoding = Check.get('encoding', encoding)
        with open(filename, 'w', encoding=encoding) as f:
            for line in content:
                print(line, file=f)
        old_feedback = Check.current_part['feedback'][:]
        yield
        new_feedback = Check.current_part['feedback'][len(old_feedback):]
        Check.current_part['feedback'] = old_feedback
        if new_feedback:
            new_feedback = ['\n    '.join(error.split('\n')) for error in new_feedback]
            Check.error('Pri vhodni datoteki {0} z vsebino\n  {1}\nso se pojavile naslednje napake:\n- {2}', filename, '\n  '.join(content), '\n- '.join(new_feedback))

    @staticmethod
    @contextmanager
    def input(content, visible=None):
        old_stdin = sys.stdin
        old_feedback = Check.current_part['feedback'][:]
        try:
            with Check.set_stringio(visible):
                sys.stdin = Check.get('stringio')('\n'.join(content) + '\n')
                yield
        finally:
            sys.stdin = old_stdin
        new_feedback = Check.current_part['feedback'][len(old_feedback):]
        Check.current_part['feedback'] = old_feedback
        if new_feedback:
            new_feedback = ['\n  '.join(error.split('\n')) for error in new_feedback]
            Check.error('Pri vhodu\n  {0}\nso se pojavile naslednje napake:\n- {1}', '\n  '.join(content), '\n- '.join(new_feedback))

    @staticmethod
    def out_file(filename, content, encoding=None):
        encoding = Check.get('encoding', encoding)
        with open(filename, encoding=encoding) as f:
            out_lines = f.readlines()
        equal, diff, line_width = Check.difflines(out_lines, content)
        if equal:
            return True
        else:
            Check.error('Izhodna datoteka {0}\n  je enaka{1}  namesto:\n  {2}', filename, (line_width - 7) * ' ', '\n  '.join(diff))
            return False

    @staticmethod
    def output(expression, content, env=None, update_env=None):
        global_env = Check.init_environment(env=env, update_env=update_env)
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        try:
            exec(expression, global_env)
        finally:
            output = sys.stdout.getvalue().strip().splitlines()
            sys.stdout = old_stdout
        equal, diff, line_width = Check.difflines(output, content)
        if equal:
            return True
        else:
            Check.error('Program izpiše{0}  namesto:\n  {1}', (line_width - 13) * ' ', '\n  '.join(diff))
            return False

    @staticmethod
    def difflines(actual_lines, expected_lines):
        actual_len, expected_len = len(actual_lines), len(expected_lines)
        if actual_len < expected_len:
            actual_lines += (expected_len - actual_len) * ['\n']
        else:
            expected_lines += (actual_len - expected_len) * ['\n']
        equal = True
        line_width = max(len(actual_line.rstrip()) for actual_line in actual_lines + ['Program izpiše'])
        diff = []
        for out, given in zip(actual_lines, expected_lines):
            out, given = out.rstrip(), given.rstrip()
            if out != given:
                equal = False
            diff.append('{0} {1} {2}'.format(out.ljust(line_width), '|' if out == given else '*', given))
        return equal, diff, line_width

    @staticmethod
    def init_environment(env=None, update_env=None):
        global_env = globals()
        if not Check.get('update_env', update_env):
            global_env = dict(global_env)
        global_env.update(Check.get('env', env))
        return global_env

    @staticmethod
    def generator(expression, expected_values, should_stop=None, further_iter=None, clean=None, env=None, update_env=None):
        from types import GeneratorType
        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get('clean', clean)
        gen = eval(expression, global_env)
        if not isinstance(gen, GeneratorType):
            Check.error("Izraz {0} ni generator.", expression)
            return False

        try:
            for iteration, expected_value in enumerate(expected_values):
                actual_value = next(gen)
                if clean(actual_value) != clean(expected_value):
                    Check.error("Vrednost #{0}, ki jo vrne generator {1} je {2!r} namesto {3!r}.",
                                iteration, expression, actual_value, expected_value)
                    return False
            for _ in range(Check.get('further_iter', further_iter)):
                next(gen)  # we will not validate it
        except StopIteration:
            Check.error("Generator {0} se prehitro izteče.", expression)
            return False
        
        if Check.get('should_stop', should_stop):
            try:
                next(gen)
                Check.error("Generator {0} se ne izteče (dovolj zgodaj).", expression)
            except StopIteration:
                pass  # this is fine
        return True

    @staticmethod
    def summarize():
        for i, part in enumerate(Check.parts):
            if not Check.has_solution(part):
                print('{0}. podnaloga je brez rešitve.'.format(i + 1))
            elif not part['valid']:
                print('{0}. podnaloga nima veljavne rešitve.'.format(i + 1))
            else:
                print('{0}. podnaloga ima veljavno rešitev.'.format(i + 1))
            for message in part['feedback']:
                print('  - {0}'.format('\n    '.join(message.splitlines())))

    settings_stack = [{
        'clean': clean.__func__,
        'encoding': None,
        'env': {},
        'further_iter': 0,
        'should_stop': False,
        'stringio': VisibleStringIO,
        'update_env': False,
    }]

    @staticmethod
    def get(key, value=None):
        if value is None:
            return Check.settings_stack[-1][key]
        return value

    @staticmethod
    @contextmanager
    def set(**kwargs):
        settings = dict(Check.settings_stack[-1])
        settings.update(kwargs)
        Check.settings_stack.append(settings)
        try:
            yield
        finally:
            Check.settings_stack.pop()

    @staticmethod
    @contextmanager
    def set_clean(clean=None, **kwargs):
        clean = clean or Check.clean
        with Check.set(clean=(lambda x: clean(x, **kwargs))
                             if kwargs else clean):
            yield

    @staticmethod
    @contextmanager
    def set_environment(**kwargs):
        env = dict(Check.get('env'))
        env.update(kwargs)
        with Check.set(env=env):
            yield

    @staticmethod
    @contextmanager
    def set_stringio(stringio):
        if stringio is True:
            stringio = VisibleStringIO
        elif stringio is False:
            stringio = io.StringIO
        if stringio is None or stringio is Check.get('stringio'):
            yield
        else:
            with Check.set(stringio=stringio):
                yield


def _validate_current_file():
    def extract_parts(filename):
        with open(filename, encoding='utf-8') as f:
            source = f.read()
        part_regex = re.compile(
            r'# =+@(?P<part>\d+)=\s*\n' # beginning of header
            r'(\s*#( [^\n]*)?\n)+?'     # description
            r'\s*# =+\s*?\n'            # end of header
            r'(?P<solution>.*?)'        # solution
            r'(?=\n\s*# =+@)',          # beginning of next part
            flags=re.DOTALL | re.MULTILINE
        )
        parts = [{
            'part': int(match.group('part')),
            'solution': match.group('solution')
        } for match in part_regex.finditer(source)]
        # The last solution extends all the way to the validation code,
        # so we strip any trailing whitespace from it.
        parts[-1]['solution'] = parts[-1]['solution'].rstrip()
        return parts

    def backup(filename):
        backup_filename = None
        suffix = 1
        while not backup_filename or os.path.exists(backup_filename):
            backup_filename = '{0}.{1}'.format(filename, suffix)
            suffix += 1
        shutil.copy(filename, backup_filename)
        return backup_filename

    def submit_parts(parts, url, token):
        submitted_parts = []
        for part in parts:
            if Check.has_solution(part):
                submitted_part = {
                    'part': part['part'],
                    'solution': part['solution'],
                    'valid': part['valid'],
                    'secret': [x for (x, _) in part['secret']],
                    'feedback': json.dumps(part['feedback']),
                }
                if 'token' in part:
                    submitted_part['token'] = part['token']
                submitted_parts.append(submitted_part)
        data = json.dumps(submitted_parts).encode('utf-8')
        headers = {
            'Authorization': token,
            'content-type': 'application/json'
        }
        request = urllib.request.Request(url, data=data, headers=headers)
        response = urllib.request.urlopen(request)
        return json.loads(response.read().decode('utf-8'))

    def update_attempts(old_parts, response):
        updates = {}
        for part in response['attempts']:
            part['feedback'] = json.loads(part['feedback'])
            updates[part['part']] = part
        for part in old_parts:
            valid_before = part['valid']
            part.update(updates.get(part['part'], {}))
            valid_after = part['valid']
            if valid_before and not valid_after:
                wrong_index = response['wrong_indices'].get(str(part['part']))
                if wrong_index is not None:
                    hint = part['secret'][wrong_index][1]
                    if hint:
                        part['feedback'].append('Namig: {}'.format(hint))


    filename = os.path.abspath(sys.argv[0])
    file_parts = extract_parts(filename)
    Check.initialize(file_parts)

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoxNzQ5NX0:1gamY4:AJ5MD6FPOg-ULKxpo4sVb_bRw3Y'
        try:
            Check.equal('stevilo_besed("Višje, hitreje, močneje!")', 3)
            Check.equal('stevilo_besed("Bu!")', 1)
            Check.equal('stevilo_besed("Matej ima tri hruške.")', 4)
            Check.equal('stevilo_besed("Eno ima za Alenko.")', 4)
            Check.equal('stevilo_besed("")', 0)
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoxNzQ5Nn0:1gamY4:Bld5tHc6zNfFl-0T3sFhUL-2ZsM'
        try:
            test_data = [
                ("koliko_samoglasnikov('Višje, hitreje, močneje')", 8),
                ("koliko_samoglasnikov('Bu!')", 1),
                ("koliko_samoglasnikov('krst')", 0),
                ("koliko_samoglasnikov('Matej ima tri hruške.')", 7),
                ("koliko_samoglasnikov('Eno ima za Alenko.')", 8),
                ("koliko_samoglasnikov('pomaranča')", 4),
                ("koliko_samoglasnikov('Tu je 7 samoglasnikov!')", 7),
                ("koliko_samoglasnikov('Buci-buc!')", 3),
                ("koliko_samoglasnikov('Mateja ima štiri hruške!')", 9),
                ("koliko_samoglasnikov('Aaaaaaaa')", 8),
                ("koliko_samoglasnikov('smrt')", 0),
            ]
            for td in test_data:
                if not Check.equal(*td):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoxNzQ5N30:1gamY4:xf_7Xf4BApTfJRC55vmbo1tkyzM'
        try:
            test_data = [
                ('vrstice("Danes\\n je lep\\ndan.\\n")', ["Danes", " je lep", "dan.", ""]),
                ('vrstice("Danes je lep dan.")', ["Danes je lep dan."]),
                ('vrstice("\\nDanes je lep dan.\\n")', ["", "Danes je lep dan.", ""]),
            ]
            for td in test_data:
                if not Check.equal(*td):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoxNzQ5OH0:1gamY4:AwQS3QV_wgn5T5qWgTjcxjktLbw'
        try:
            Check.equal("je_haiku('Bu!')", False)
            Check.equal("je_haiku('Srečna ljubezen\\nje kot svobodna ptica,\\nki je vesela.')", True)
            Check.equal("je_haiku('Skrit v svojem svetu,\\ntemna otožnost neba,\\ntvoj topli objem.')", True)
            Check.equal("je_haiku('Riba,\\nraca, rak,\\nvinjak je grenak!')", False)
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoxNzQ5OX0:1gamY4:Yg7MIjmhw3AGf_o7XlHoB2GHvq8'
        try:
            test_data = [
                ('podcrtaj("Jaz _sem_ pa cajzelc!")', 'Jaz sem pa cajzelc!\n    ---            '),
                ('podcrtaj("_Podčrtajmo_ povedek!")', 'Podčrtajmo povedek!\n----------         '),
                ('podcrtaj("Zdaj _pa_ predlog!")', 'Zdaj pa predlog!\n     --         '),
                ('podcrtaj("_Zdaj pa vse!")', 'Zdaj pa vse!\n------------'),
                ('podcrtaj("__")', '\n'),
                ('podcrtaj("_a_")', 'a\n-'),
                ('podcrtaj("Nič")', 'Nič\n   '),
                ('podcrtaj("__AAA__")', 'AAA\n   '),
                ('podcrtaj("A__A")', 'AA\n  '),
                ('podcrtaj("_T__X_")', 'TX\n--'),
                ('podcrtaj("__T__X_")', 'TX\n  '),
            ]
            for td in test_data:
                if not Check.equal(*td):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoxNzUwMH0:1gamY4:HwoLCHvaX9DVitMGGMyi_Y8FW3s'
        try:
            test_data = [
                ("""stevilo_znakov('Višje, hitreje, močneje!')""", 22),
                ("""stevilo_znakov('Bu!')""", 3),
                ("""stevilo_znakov('Matej ima tri hruške!')""", 18),
                ("""stevilo_znakov('Eno ima za Alenko.')""", 15),
                ("""stevilo_znakov('   ')""", 0),
            ]
            for td in test_data:
                if not Check.equal(*td):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoxNzUwMX0:1gamY4:rqkCKv6b3K12qgvfBmsfejx5LV8'
        try:
            test_data = [
                ("je_sonet(\"Poet tvoj nov Slovencam venec vije,\\n'z petnajst sonetov ti tako ga spleta,\\nde 'magistrale', pesem trikrat peta,\\nvseh drugih skupej veže harmonije.\\n\\nIz njega zvira, vanjga se spet zlije\\npo versti pesem vsacega soneta;\\nprihodnja v prednje koncu je začeta;\\nenak je pevec vencu poezije:\\n\\nvse misli zvirajo 'z ljubezni ene,\\nin kjer ponoči v spanji so zastale,\\nzbude se, ko spet zarja noč prežene.\\n\\nTi si življenja moj'ga magistrale,\\nglasil se 'z njega, ko ne bo več mene,\\nran mojih bo spomin in tvoje hvale.\")", True),
                ("je_sonet(\"Bolj slab\\nsonet.\\n\\nZa umret!\")", False),
            ]
            for td in test_data:
                if not Check.equal(*td):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    print('Shranjujem rešitve na strežnik... ', end="")
    try:
        url = 'https://www.projekt-tomo.si/api/attempts/submit/'
        token = 'Token ac797f2c53c7c90311d269162e2f70771b1d5202'
        response = submit_parts(Check.parts, url, token)
    except urllib.error.URLError:
        print('PRI SHRANJEVANJU JE PRIŠLO DO NAPAKE! Poskusite znova.')
    else:
        print('Rešitve so shranjene.')
        update_attempts(Check.parts, response)
        if 'update' in response:
            print('Posodabljam datoteko... ', end="")
            backup_filename = backup(filename)
            with open(__file__, 'w', encoding='utf-8') as f:
                f.write(response['update'])
            print('Stara datoteka je bila preimenovana v {0}.'.format(backup_filename))
            print('Če se datoteka v urejevalniku ni osvežila, jo zaprite ter ponovno odprite.')
    Check.summarize()

if __name__ == '__main__':
    _validate_current_file()
