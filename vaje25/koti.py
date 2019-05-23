# =============================================================================
# Koti
# =====================================================================@021085=
# 1. podnaloga
# Sestavi razred `Kot` z začetno metodo `__init__(self, st, m, sek)`, ki
# predstavlja kot podane velikosti. Podatke shranite v atribute `stopinje`,
# `minute` in `sekunde`, pri tem pa minute in sekunde večje od 60 ustrezno
# pretvorite.
# 
# Primer:
# 
#     >>> a = Kot(15, 65, 100)
#     >>> a.sekunde
#     40
#     >>> a.minute
#     6
#     >>> a.stopinje
#     16
# =============================================================================
class Kot:
    def __init__(self, st, m, sek):
        while sek >= 60:
            m += 1
            sek -= 60
        while m >= 60:
            st += 1
            m -= 60
        self.stopinje = st
        self.minute = m
        self.sekunde = sek
# =====================================================================@021086=
# 2. podnaloga
# Razredu Kot dodaj metodo `__str__`, ki kot predstavi v berljivi obliki
# `kot° minute' sekunde''`.
# 
# Primer:
# 
#     >>> a = Kot(15, 65, 100)
#     >>> print(a)
#     16° 6' 40''
# =============================================================================
class Kot(Kot):
    def __str__(self):
        return str(self.stopinje)+'° '+str(self.minute)+"' " + str(self.sekunde)+"''"
# =====================================================================@021087=
# 3. podnaloga
# Razredu dodaj metodo `__repr__`, ki vrne predstavitev razreda kot niz oblike
# `Kot(st, m, s)`, kjer so `st`, `m` in `s` stopinje, minute in sekunde kota.
# 
# Primer:
# 
#     >>> a = Kot(15, 65, 100)
#     >>> a
#     Kot(16, 6, 40)
# =============================================================================
class Kot(Kot):
    def __repr__(self):
        return 'Kot({0}, {1}, {2})' .format(self.stopinje, self.minute, self.sekunde)
# =====================================================================@021088=
# 4. podnaloga
# Razredu dodaj metodo `__lt__(self, other)`, ki primerja dva kota med seboj.
# Metoda naj vrne `True`, če je prvi kot manjši od drugega. Kota lahko nato
# primerjamo z operatorjem `<`.
# 
# Primer:
# 
#     >>> a = Kot(15, 65, 100)
#     >>> b = Kot(10, 20, 30)
#     >>> a < b
#     False
# =============================================================================
class Kot(Kot):
    def __lt__(self, other):
        return (self.stopinje,self.minute,self.sekunde) < (other.stopinje, other.minute, other.sekunde)
        
# =====================================================================@021089=
# 5. podnaloga
# Razredu dodaj metodo `__eq__(self, other)`, ki vrne `True`, če sta dva kota
# enaka.
# 
# Primer:
# 
#     >>> a = Kot(15, 65, 100) == Kot(16, 6, 40)
#     True
# =============================================================================
class Kot(Kot):
    def __eq__(self, other):
        a = Kot(self.stopinje, self.minute, self.sekunde)
        b = Kot(other.stopinje, other.minute, other.sekunde)
        if str(a) == str(b):
            return True
        return False
# =====================================================================@021090=
# 6. podnaloga
# Razredu dodaj metodo `__add__(self, other)`, ki sešteje dva kota.
# 
# Primer:
# 
#     >>> a = Kot(15, 65, 100)
#     >>> b = Kot(10, 20, 30)
#     >>> a + b
#     Kot(26, 27, 10)
# =============================================================================
class Kot(Kot):
    def __add__(self, other):
        stopinje = self.stopinje + other.stopinje
        minute = self.minute + other.minute
        sekunde = self.sekunde + other.sekunde
        return Kot(stopinje, minute, sekunde)
# =====================================================================@021091=
# 7. podnaloga
# Razredu dodaj metodo `get(self)`, ki vrne trojko `(st, m, sek)`.
# 
# Primer:
# 
#     >>> Kot(15, 65, 100).get()
#     (16, 6, 40)
# =============================================================================
class Kot(Kot):
    def get(self):
        kot = Kot(self.stopinje, self.minute, self.sekunde)
        return (kot.stopinje, kot.minute, kot.sekunde)
# =====================================================================@021092=
# 8. podnaloga
# Zunaj razreda sestavi funkcijo `suplementaren(kot)`, ki vrne trojko 
# (stopinje, minute, sekunde) kota, ki je suplementaren danemu kotu. Podatke
# kota `kot` pridobi s klicem metode get. Če je dani kot večji od 180°, naj
# funkcija vrne `None`
# 
# Primer:
# 
#     >>> a = Kot(10, 20, 30)
#     >>> suplementaren(a)
#     (169, 39, 30)
# =============================================================================
def suplementaren(kot):
    objekt = kot.get()
    stopinj, minut, sekund = objekt[0], objekt[1], objekt[2]

    if stopinj > 180:
        return None
    return Kot(180 - 1  - stopinj, 60 - 1 - minut, 60  - sekund).get()
# =====================================================================@021093=
# 9. podnaloga
# Našemu razredu bi radi dodali še metodo `povecaj` in `pomnozi`, ki naš kot
# spremeni (ne vrne novega kota, ampak ustrezno spremeni atribute začetnega
# kota). Pri obeh metodah bi morali posebej obravnavati primere, ko dobimo
# prevelike minute ali sekunde. Da bo računanje enostavneje sestavi nov razred
# `Kot2`. Začetna metoda `__init__(self, st, m, sek)` stopinje in minute
# spremeni v sekunde in celotno vrednost shrani v atribut sekunde.
# 
# Primer:
# 
#     >>> a = Kot2(15, 15, 15)
#     >>> a.sekunde
#     54915
# =============================================================================
class Kot2:
    def __init__(self, st, m, sek):
        sek += (st * 60**2) + m*60
        self.sekunde = sek
        self.minute = m
        self.stopinje = st
        
# =====================================================================@021095=
# 10. podnaloga
# Razredu Kot2 dodaj metodi `povecaj(self, st, m, sek)` in `pomnozi(self,
# stevilo)`. Metoda `povecaj` naj dani kot poveča za `st` stopinj, `m` minut in
# `sek` sekund, metoda `pomnozi` pa naj dani kot pomnozi z danim številom.
# 
# Primer:
# 
#     >>> a = Kot2(15, 15, 15)
#     >>> a.povecaj(10, 20, 30)
#     >>> a.sekunde
#     92145
#     >>> a.pomnozi(2)
#     >>> a.sekunde
#     184290
# =============================================================================
class Kot2(Kot2):
    def povecaj(self, st, m, sek):
        self.sekunde += Kot2(st, m, sek).sekunde
        return self.sekunde
    def pomnozi(self, stevilo):
        self.sekunde *= stevilo
# =====================================================================@021094=
# 11. podnaloga
# Razredu Kot2 dodaj metodo `get`, ki naj vrne enako predstavitev kota kot v
# razredu Kot. Ko bo metoda dodana, bo funkcija suplementaren delovala tudi za
# kote iz razreda Kot2.
# 
# Primer:
# 
#     >>> a = Kot2(15, 15, 15)
#     >>> a.get()
#     (15, 15, 15)
#     >>> suplementaren(Kot2(115, 5, 40))
#     (64, 54, 20)
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
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoyMTA4NX0:1hTh8L:xla-FFkfCaBhPV4Wka_DAgG1zcw'
        try:
            testi = [
                ('Kot(15, 30, 45).stopinje', 15),
                ('Kot(15, 30, 45).minute', 30),
                ('Kot(15, 30, 45).sekunde', 45),
                ('Kot(15, 175, 100).sekunde', 40),
                ('Kot(15, 175, 100).minute', 56),
                ('Kot(15, 175, 100).stopinje', 17),
            ]
            
            for test in testi:
                if not Check.equal(*test):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoyMTA4Nn0:1hTh8L:H4cdRvWAbSn0zI_8-x6B6tZ7lzA'
        try:
            testi = [
                ('str(Kot(15, 30, 45))', "15° 30' 45''"),
                ('str(Kot(15, 65, 100))', "16° 6' 40''"),
                ('str(Kot(15, 175, 100))', "17° 56' 40''")
            ]
            
            for test in testi:
                if not Check.equal(*test):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoyMTA4N30:1hTh8L:x_r5ucHfJWPUYAGXrw5TVnIqSw4'
        try:
            testi = [
                ('repr(Kot(15, 30, 45))', "Kot(15, 30, 45)"),
                ('repr(Kot(15, 65, 100))', "Kot(16, 6, 40)"),
                ('repr(Kot(15, 175, 100))', "Kot(17, 56, 40)")
            ]
            
            for test in testi:
                if not Check.equal(*test):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoyMTA4OH0:1hTh8L:BV5QVL8lyBVJiQqqsyBAaTJ4Rds'
        try:
            testi = [
                ('Kot(15, 65, 100) < Kot(10, 20, 30)', False),
                ('Kot(65, 50, 25) < Kot(100, 50, 20)', True),
                ('Kot(10, 60, 70) < Kot(11, 1, 10)', False)
            ]
            
            for test in testi:
                if not Check.equal(*test):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoyMTA4OX0:1hTh8L:jhyrWzZ3VUx522xH2LoAKRQj1aI'
        try:
            testi = [
                ('Kot(15, 65, 100) == Kot(10, 20, 30)', False),
                ('Kot(65, 50, 25) == Kot(100, 50, 20)', False),
                ('Kot(10, 60, 70) == Kot(11, 1, 10)', True),
                ('Kot(15, 65, 100) == Kot(16, 6, 40)', True),
                ('Kot(11, 1, 10) == Kot(11, 1, 10)', True)
            ]
            
            for test in testi:
                if not Check.equal(*test):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoyMTA5MH0:1hTh8L:ETfmfYkc81bwM62ABcN0LKrpUbk'
        try:
            testi = [
                ('Kot(15, 65, 100) + Kot(10, 20, 30)', Kot(26, 27, 10)),
                ('Kot(65, 50, 25) + Kot(100, 50, 20)', Kot(166, 40, 45)),
                ('Kot(10, 60, 70) + Kot(11, 1, 10)', Kot(22, 2, 20))
            ]
            
            for test in testi:
                if not Check.equal(*test):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoyMTA5MX0:1hTh8L:00ViaXPIh9h6eRK6QZL-v-aaNKA'
        try:
            testi = [
                ('Kot(15, 65, 100).get()', (16, 6, 40)),
                ('Kot(65, 50, 25).get()', (65, 50, 25)),
                ('Kot(10, 60, 70).get()', (11, 1, 10))
            ]
            
            for test in testi:
                if not Check.equal(*test):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoyMTA5Mn0:1hTh8L:0YbHVTrVHgrrbvDOlNbhvvx_eOA'
        try:
            testi = [
                ('suplementaren(Kot(115, 5, 40))', (64, 54 ,20)),
                ('suplementaren(Kot(10, 20, 30))', (169, 39, 30)),
                ('suplementaren(Kot(65, 50, 0))', (114, 10, 0)),
                ('suplementaren(Kot(11, 0, 0))', (169, 0, 00)),
                ('suplementaren(Kot(180, 0, 0))', (0, 0, 0)),
                ('suplementaren(Kot(0, 0, 0))', (180, 0, 0)),
                ('suplementaren(Kot(191, 1, 10))', None),  
            ]
            
            for test in testi:
                if not Check.equal(*test):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoyMTA5M30:1hTh8L:STQtm7ATvdTlMDieZWJn9z2HMoo'
        try:
            testi = [
                ('Kot2(15, 30, 45).sekunde', 55845),
                ('Kot2(15, 175, 100).sekunde', 64600),
                ('Kot2(15, 15, 15).sekunde', 54915),
            ]
            
            for test in testi:
                if not Check.equal(*test):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoyMTA5NX0:1hTh8L:o-xYWowlXNRiXpRHb7Yzy1HSOuo'
        try:
            Check.run(["a = Kot2(15, 15, 15)", "a.povecaj(10, 20, 30)", "s = a.sekunde"],
                      {'s': 92145})
            
            Check.run(["a = Kot2(10, 20, 30)", "a.pomnozi(3)", "s = a.sekunde"],
                      {'s': 111690})
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoyMTA5NH0:1hTh8L:29_-7_5W3RS5tImkz1NpOhgRPfM'
        try:
            testi = [
                ('Kot2(15, 30, 45).get()', (15, 30, 45)),
                ('suplementaren(Kot2(115, 5, 40))', (64, 54, 20))
            ]
            
            for test in testi:
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
