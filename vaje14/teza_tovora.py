# =============================================================================
# Teža tovora
#
# Dan je slovar, ki hrani podatke o tem, kakšen tovor smo naložili na tovornjak
# in kolikšna je masa posameznih kosov tovora. Na primer, slovar
# 
#       {'televizor' : 17, 'zaboj piva' : 12, 'zofa' : 35}
# 
# pove, da smo na tovornjak naložili 17kg težak televizor, 12kg težak zaboj piva
# in 35kg težko zofo.
# =====================================================================@019500=
# 1. podnaloga
# Sestavi funkcijo `masa_tovora(tovor)`, ki sprejme tak slovar in vrne skupno
# maso tovora (v našem primeru 17 + 12 + 35 = 64 kg).
# =============================================================================
def masa_tovora(tovor):
    vsota = 0
    for key, val in tovor.items():
        vsota = vsota + val
    return vsota
# =====================================================================@019501=
# 2. podnaloga
# Sestavi funkcijo `lahko_pelje(tovor, nosilnost)`, ki ugotovi, ali tovornjak
# z nosilnostjo `nosilnost` lahko pelje tovor, dan s slovarjem `tovor`.
# =============================================================================
def lahko_pelje(tovor,nosilnost):
    vsota = 0
    for key, val in tovor.items():
        vsota = vsota + val
    if nosilnost >= vsota:
        return True
    return False
# =====================================================================@019502=
# 3. podnaloga
# Sestavi funkcijo `enaka_tovora(tovor1, tovor2)`, ki ugotovi, če sta
# tovora, podana v slovarjih `tovor1` in `tovor2` enaka! Tovora sta enaka, če
# vsebujeta enake predmete z isto maso.
# =============================================================================
def enaka_tovora(tovor1, tovor2):

    if len(tovor1) != len(tovor2):
        return False
    for key, val in tovor1.items():
        if key in tovor2 and tovor2[key] == val:
            pass
        else:
            return False

    return True
# =====================================================================@019503=
# 4. podnaloga
# Sestavi funkcijo `smiselen_tovor(tovor, min_masa, max_masa)`, ki "prečisti"
# slovar z danimi masami tako, da vrne slovar, v katerem so le tisti predmeti,
# katerih masa je med `min_masa` in `max_masa`.
# =============================================================================
def smiselen_tovor(tovor, min_masa, max_masa):
    tab_key = []
    for key, val in tovor.items():
        if min_masa <= val <= max_masa:
            pass
        else:
            tab_key.append(key)

    for key in tab_key:
        del tovor[key]
    return tovor
# =====================================================================@019504=
# 5. podnaloga
# Sestavi funkcijo `najdaljsi_opis(tovor)`, ki vrne po abecedi urejeno
# tabelo tistih predmetov, ki imajo najdaljši opis.
# Za slovar iz zgleda bi torej dobili `['zaboj piva']`
# =============================================================================
def najdaljsi_opis(tovor):
    '''funkcija vrne najdaljsi kljuc v slovarju'''
    tab = []
    naj_d = 0
    for key, val in tovor.items():
        if len(key) >= naj_d:
            naj_d = len(key)
    for key, val in tovor.items():
        if len(key) == naj_d:
            tab.append(key)
    tab.sort()
    return tab
# =====================================================================@019505=
# 6. podnaloga
# Sestavi funkcijo `najlazji_predmet(tovor)`, ki vrne po abecedi urejeno
# tabelo tistih predmetov, ki so najlažji.
# Za slovar iz zgleda bi torej spet dobili `['zaboj piva']`, za prazen slovar
# pa seveda vrnemo prazno tabelo.
# =============================================================================
import collections

def najlazji_predmet(tovor):
    ''' funkcija vrne najlažje predmete, alfabetno urejene'''
    urejen_tovor = {}
    naj_m = 1029830183019283018203812038210983
    for key, val in tovor.items():
        if int(val) < naj_m:
            naj_m = int(val)
    for key, val in tovor.items():
        if int(val) != naj_m:
            pass
        else:
            urejen_tovor[key] = val
    urejen_tovor = sorted(list(urejen_tovor))
    return urejen_tovor



































































































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
        Check.current_part['token'] = 'eyJwYXJ0IjoxOTUwMCwidXNlciI6MzM2N30:1gzHOo:aPjP7RjrggsxTOPDwA7cGWAmib4'
        try:
            tovor1 = {'televizor': 17, 'zaboj piva': 12, 'zofa': 35}
            tovor2 = {'Predmet' + str(i): i for i in range(10)}
            Check.secret(masa_tovora(tovor1), tovor1)
            Check.secret(masa_tovora(tovor2), tovor2)
            Check.equal("masa_tovora({})", 0)
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoxOTUwMSwidXNlciI6MzM2N30:1gzHOo:wsGG8jdSlBLQcFNTNo-jq4DfAJg'
        try:
            tovor1 = {'televizor' : 17, 'zaboj piva' : 12, 'zofa' : 35}
            tovor2 = {'Predmet' + str(i) : i for i in range(10)}
            
            tests = [
                    ("lahko_pelje({}, 100)", True),
                    ("lahko_pelje({'kavč':100}, 100)", True),
                    ("lahko_pelje({'kavč':100}, 99)", False),
                    ("lahko_pelje({'kavč':100, 'pivo':1}, 99)", False),
                    ("lahko_pelje({'kavč':100, 'pivo':1}, 101)", True)
                    ]
            
            for test in tests:
                if not Check.equal(*test):
                    break
            
            Check.secret(lahko_pelje(tovor1, 20), (tovor1, 20))
            Check.secret(lahko_pelje(tovor1, 100), (tovor1, 100))
            Check.secret(lahko_pelje(tovor2, 45), (tovor2, 45))
            Check.secret(lahko_pelje(tovor2, -45), (tovor2, -45))
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoxOTUwMiwidXNlciI6MzM2N30:1gzHOo:lR0GnzDnGl5ssHuiGyzd76Mm9s0'
        try:
            tovor1 = {'televizor' : 17, 'zaboj piva' : 12, 'zofa' : 35}
            tovor2 = {'Predmet' + str(i) : i for i in range(10)}
            tovor3 = {'Predmet' + str(i) : 9 - i for i in range(10)}
            tovor4 = {'Predmet' + str(i) : i for i in range(10)}
            tovor5 = {'Predmet' + str(i) : i for i in range(11)}
            Check.secret(enaka_tovora(tovor3, tovor2), (tovor3, tovor2))
            Check.secret(enaka_tovora(tovor2, tovor5), (tovor2, tovor5))
            Check.secret(enaka_tovora(tovor2, tovor4), (tovor2, tovor4))
            Check.secret(enaka_tovora(tovor2, tovor3), (tovor2, tovor3))
            
            tests = [
                    ("enaka_tovora({'televizor' : 17, 'zaboj piva' : 12, 'zofa' : 35}, {'televizor' : 17, 'zaboj piva' : 12, 'zofa' : 35})", True),
                    ("enaka_tovora({}, {})", True),
                    ("enaka_tovora({'televizor' : 17, 'zaboj piva' : 12, 'zofa' : 35}, {'zaboj piva' : 12, 'televizor' : 17, 'zofa' : 35})", True),
                    ("enaka_tovora({'televizor' : 17, 'zaboj piva' : 12, 'zofa' : 35}, {'televizor' : 17, 'zaboj piva' : 12, 'zofa' : 35})", True),
                    ("enaka_tovora({'televizor' : 17, 'zaboj piva' : 12, 'zofa' : 35}, {'zaboj piva' : 12, 'zofa' : 35})", False),
                    ("enaka_tovora({'zaboj piva' : 12, 'zofa' : 35}, {'televizor' : 17, 'zaboj piva' : 12, 'zofa' : 35})", False),
                    ("enaka_tovora({'televizor' : 17, 'zaboj piva' : 12, 'zofa' : 35}, {'televizor' : 17, 'zaboj piva' : 12, 'zofa' : 100})", False)
                    ]
            
            for test in tests:
                if not Check.equal(*test):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoxOTUwMywidXNlciI6MzM2N30:1gzHOo:lPH-9re0TkpAYPBFXm8xD-G-x18'
        try:
            tests = [
                    ("smiselen_tovor({'televizor' : 17, 'zaboj piva' : 12, 'zofa' : 35}, 20, 100)", {'zofa' : 35}),
                    ("smiselen_tovor({'televizor' : 17, 'zaboj piva' : 12, 'zofa' : 35}, 10, 100)", tovor1),
                    ("smiselen_tovor({'televizor' : 17, 'zaboj piva' : 12, 'zofa' : 35}, 10, 15)", {'zaboj piva' : 12}),
                    ("smiselen_tovor({'televizor' : 17, 'zaboj piva' : 12, 'zofa' : 35}, 10, 10)", {}),
                    ("smiselen_tovor({'televizor' : 17, 'zaboj piva' : 12, 'zofa' : 35}, 12, 12)", {'zaboj piva' : 12}),
                    ("smiselen_tovor({}, 10, 15)", {})
                    ]
            
            for test in tests:
                if not Check.equal(*test):
                    break
            
            tovor2 = {'Predmet' + str(i) : i for i in range(10)}
            tovor3 = {'Predmet' + str(i) : 9 - i for i in range(10)}
            Check.secret(smiselen_tovor(tovor2, 0, 2), (tovor2, 0, 2))
            Check.secret(smiselen_tovor(tovor3, 0, 2), (tovor3, 0, 2))
            Check.secret(smiselen_tovor(tovor2, 2, 2), (tovor2, 2, 2))
            Check.secret(smiselen_tovor(tovor3, 2, 2), (tovor3, 2, 2))
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoxOTUwNCwidXNlciI6MzM2N30:1gzHOo:v3KwXg44794TWoMxzK5c1FMtol0'
        try:
            tests = [
                    ("najdaljsi_opis({'televizor' : 17, 'zaboj piva' : 12, 'zofa' : 35})", ['zaboj piva']),
                    ("najdaljsi_opis({})", []),
                    ("najdaljsi_opis({'televizor' : 17, 'zaboj piva' : 12, 'zofa' : 35, 'ZABOJ piva' : 12})", ['ZABOJ piva','zaboj piva']),
                    ("najdaljsi_opis({'a' : 17, 'c' : 12, 'b' : 35, 'x' : 12})", ['a', 'b', 'c', 'x'])
                    ]
            
            for test in tests:
                if not Check.equal(*test):
                    break
            
            tovor2 = {'Predmet' + str(i): i for i in range(10)}
            tovor3 = {'televizor': 17, 'zaboj piva': 12, 'zofa': 35,
                      'televizia': 17, 'Zaboj piva': 12, 'sofa': 35,
                      'Televizor': 17, 'gajba pira': 12, 'kavč': 35}
            Check.secret(najdaljsi_opis(tovor2), tovor2)
            Check.equal("najdaljsi_opis(tovor3)", sorted(['zaboj piva','Zaboj piva', 'gajba pira']),
                        env={'tovor3': tovor3})
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoxOTUwNSwidXNlciI6MzM2N30:1gzHOo:bOPn6-KdY36HcC0zxyMWnmwVEXE'
        try:
            tests = [
                    ("najlazji_predmet({'televizor' : 17, 'zaboj piva' : 12, 'zofa' : 35})", ['zaboj piva']),
                    ("najlazji_predmet({})", []),
                    ("najlazji_predmet({'znanje' : 12, 'televizor' : 17, 'zaboj piva' : 12, 'zofa' : 35, 'ZABOJ piva' : 12, 'mleko' : 12})",
                        ['ZABOJ piva', 'mleko', 'zaboj piva', 'znanje']),
                    ("najlazji_predmet({'a' : 12, 'c' : 12, 'b' : 12, 'x' : 12})", ['a', 'b', 'c', 'x']),
                    ("najlazji_predmet({'a' : 12, 'c' : 12, 'b' : 12, 'x' : 12, 'd': 12})", ['a', 'b', 'c', 'd', 'x'])
                    ]
            
            for test in tests:
                if not Check.equal(*test):
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
