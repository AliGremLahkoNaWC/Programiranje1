# =============================================================================
# Ulomki
#
# POZOR:
# 
# Da ne bo težav pri testiranju, pri vseh podnalogah začnemo z
# 
#                   class Ulomek(Ulomek):
# 
# To pomeni, da se v razred "skopirajo" vse definicije, ki ste jih
# v razred Ulomek napisali prej. Seveda pa 1. podnalogo še vedno začnemo z
# 
#                   class Ulomek:
# 
# Druga možnost pa je, da podnaloge vedno začnemo z
# 
#                   class Ulomek:
# 
# a potem v razred vedno napišemo vse metode, ki smo jih definirali v
# vseh prejšnjih podnalogah!
# =====================================================================@021038=
# 1. podnaloga
# Sestavite razred `Ulomek`, s katerim predstavimo ulomek. Števec in
# imenovalec sta celi števili, pri čemer je imenovalec vedno pozitiven.
# Ulomki naj bodo vedno okrajšani. Števec naj bo v atributu `st` in imenovalec
# v atributu `im`. Če vnesemo za imenovalec število 0, naj inicializacijska metoda javi
# napako.
# 
# Sestavite metodo `__init__(self, toJeStevec, toJeImenovalec)`. Zgled:
# 
#     >>> u = Ulomek(5, -20)
#     >>> u.st
#     -1
#     >>> u.im
#     4
# 
# Namig: največji skupni imenovalec izračuna funkcija
# [`math.gcd`](https://docs.python.org/3/library/math.html).
# =============================================================================
class Ulomek:

    def __init__(self, toJeStevec, toJeImenovalec):
        import math
        if toJeImenovalec == 0:
            raise ZeroDivisionError
        gcd = math.gcd(toJeStevec, toJeImenovalec)
        toJeStevec, toJeImenovalec = toJeStevec // gcd, toJeImenovalec // gcd
        if abs(toJeStevec) != toJeStevec and abs(toJeImenovalec) != toJeImenovalec:
            self.st = abs(toJeStevec)
            self.im = abs(toJeImenovalec)
        elif abs(toJeStevec) == toJeStevec and abs(toJeImenovalec) != toJeImenovalec:
            self.st = -1 * toJeStevec
            self.im = abs(toJeImenovalec)
        else:
            self.st = toJeStevec
            self.im = toJeImenovalec


# =====================================================================@021039=
# 2. podnaloga
# Trenutna implementacija razreda `Ulomek` objekt `Ulomek(5, 20)` izpiše z nizom
# oblike `<__main__.Ulomek object at 0x000002CB41CDD2B0>`, iz katerega ne moremo
# razbrati za kateri ulomek gre. Kako naj se objekt našega razreda izpiše, lahko
# sami določimo z metodama `__str__` in `__repr__`. Kako metodi delujeta in
# kakšna je razlika med njima si poglejte v
# [videu](https://dbader.org/blog/python-repr-vs-str).
# 
# Sestavite metodo  `__str__(self)`, ki predstavi ulomek z nizom
# oblike `'st/im'`. Zgled:
# 
#     >>> u = Ulomek(5, 20)
#     >>> print(u)
#     1/4
# =============================================================================
class Ulomek(Ulomek):
    def __str__(self):
        return '{self.st}/{self.im}' .format(self = self)
# =====================================================================@021040=
# 3. podnaloga
# Sestavite še metodo  `__repr__(self)`, ki predstavi ulomek z nizom
# oblike `'Ulomek(st, im)'`. Zgled:
# 
#     >>> u = Ulomek(5, 20)
#     >>> u
#     Ulomek(1, 4)
# =============================================================================
class Ulomek(Ulomek):
    def __repr__(self):
        return 'Ulomek({0}, {1})' .format(self.st, self.im)
# =====================================================================@021041=
# 4. podnaloga
# Sestavite metodo  `__eq__(self, other)`, ki vrne `True` če sta dva
# ulomka enaka, in `False` sicer. Ko definirate to metodo, lahko ulomke
# primerjate kar z operatorjem `==`. Zgled:
# 
#     >>> Ulomek(1, 3) == Ulomek(2, 3)
#     False
#     >>> Ulomek(2, 3) == Ulomek(10, 15)
#     True
# 
# Lahko prepodstavite, da je drugi parameter (desni operand pri ==) zagotovo objekt
# iz razreda `Ulomek`.
# =============================================================================
class Ulomek(Ulomek):
    def __eq__(self, other):
        if repr(self) != repr(other):
            return False
        return True
# =====================================================================@021042=
# 5. podnaloga
# Sestavite metodo  `__add__(self, other)`, ki vrne vsoto dveh ulomkov.
# Ko definirate to metodo, lahko ulomke seštevate kar z operatorjem `+`.
# Na primer:
# 
#     >>> Ulomek(1, 6) + Ulomek(1, 4)
#     Ulomek(5, 12)
# 
# Lahko prepodstavite, da je drugi parameter (operand pri +) zagotovo objekt iz razreda
# `Ulomek`.
# =============================================================================
class Ulomek(Ulomek):
    def __add__(self, other):
        if self.im > other.im:
            greater = self.im
        else:
            greater = other.im
        while(True):
            if((greater % self.im == 0) and (greater % other.im == 0)):
                lcm = greater
                break
            greater += 1
        #sposojena koda

        b = lcm
        a = (b//self.im)*self.st + (b//other.im)*other.st
        return Ulomek(a,b)

# =====================================================================@021043=
# 6. podnaloga
# Sestavite metodo  `__sub__(self, other)`, ki vrne razliko dveh ulomkov.
# Ko definirate to metodo, lahko ulomke odštevate kar z operatorjem `-`.
# Na primer:
# 
#     >>> Ulomek(1, 4) - Ulomek(1, 6)
#     Ulomek(1, 12)
# 
# Lahko prepodstavite, da je drugi parameter (desni operand pri -) zagotovo objekt
# iz razreda `Ulomek`.
# =============================================================================
class Ulomek(Ulomek):
    def __sub__(self, other):
        if self.im > other.im:
            greater = self.im
        else:
            greater = other.im
        while(True):
            if((greater % self.im == 0) and (greater % other.im == 0)):
                lcm = greater
                break
            greater += 1
        #sposojena koda

        b = lcm
        a = (b//self.im)*self.st - (b//other.im)*other.st
        return Ulomek(a,b)
# =====================================================================@021044=
# 7. podnaloga
# Sestavite metodo  `__mul__(self, other)`, ki vrne zmnožek dveh ulomkov.
# Ko definirate to metodo, lahko ulomke množite kar z operatorjem `*`.
# Na primer:
# 
#     >>> Ulomek(1, 3) * Ulomek(1, 2)
#     Ulomek(1, 6)
# 
# Lahko prepodstavite, da je drugi parameter (desni operand pri *) zagotovo objekt
# iz razreda `Ulomek`.
# =============================================================================
class Ulomek(Ulomek):
    def __mul__(self, other):
        a = self.st * other.st
        b = self.im * other.im
        return Ulomek(a, b)
# =====================================================================@021045=
# 8. podnaloga
# Sestavite metodo  `__truediv__(self, other)`, ki vrne kvocient dveh
# ulomkov. Ko definirate to metodo, lahko ulomke delite kar z operatorjem
# `/`. Na primer:
# 
#     >>> Ulomek(1, 6) / Ulomek(1, 4)
#     Ulomek(2, 3)
# 
# (Videli smo nekaj t.i. magičnih metod, seznam preostali pa si lahko pogledaš
# npr. [tukaj](https://www.tutorialsteacher.com/python/magic-methods-in-python).)
# =============================================================================
class Ulomek(Ulomek):
    def __truediv__(self, other):
        a = self.st * other.im
        b = self.im * other.st
        return Ulomek(a, b)
# =====================================================================@021046=
# 9. podnaloga
# Izven razreda `Ulomek` definirajte funkcijo `priblizek(n)`, ki vrne
# vsoto $$\frac{1}{0!} + \frac{1}{1!} + \frac{1}{2!} + … + \frac{1}{n!}.$$
# Funkcija naj uporablja razred `Ulomek`. Zgled:
# 
#     >>> priblizek(5)
#     Ulomek(163, 60)
# 
# Ali je izračunana vrednost blizu števila $e$?
# =============================================================================
def priblizek(n):
    '''vrne vsoto ulomkov s faktorialnimi imenovalci'''
    i = 0
    while i <= n




































































































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
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoyMTAzOH0:1hR9zk:WQ9uVgaXLyzhF2zgoTbXRIV240s'
        try:
            tests = [
                    ('Ulomek(5, 1).st', 5),
                    ('Ulomek(5, 1).im', 1),
                    ('Ulomek(5, 20).st', 1),
                    ('Ulomek(5, 20).im', 4),
                    ('Ulomek(20, 6).st', 10),
                    ('Ulomek(20, 6).im', 3),
                    ('Ulomek(5, 7).st', 5),
                    ('Ulomek(5, 7).im', 7),
                    ('Ulomek(7, 5).st', 7),
                    ('Ulomek(7, 5).im', 5),
                    ('Ulomek(-7, 5).st', -7),
                    ('Ulomek(-7, 5).im', 5),
                    ('Ulomek(-7, -5).st', 7),
                    ('Ulomek(-7, -5).im', 5),
                    ('Ulomek(0, 7).st', 0),
                    ('Ulomek(0, 7).im', 1),
                    ('Ulomek(40, -60).im', 3),
                    ('Ulomek(40, -60).st', -2),
                    ('Ulomek(20, 6).st', 10),
                    ('Ulomek(20, 6).im', 3),
                    ('Ulomek(40, -60).im', 3),
                    ('Ulomek(40, -60).st', -2),
                    ('Ulomek(-40, -60).st', 2)
                    ]
            
            for test in tests:
                if not Check.equal(*test):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoyMTAzOX0:1hR9zk:6uE_V3WQ4Da8RAr_XKU4zE6ucWs'
        try:
            tests = [
                    ('str(Ulomek(20, 6))', '10/3'),
                    ('str(Ulomek(0, 113))', '0/1'),
                    ('str(Ulomek(40, -60))', '-2/3'),
                    ('str(Ulomek(5, 20))', '1/4'),
                    ('str(Ulomek(5, 7))', '5/7'),
                    ('str(Ulomek(7, 5))', '7/5'),
                    ('str(Ulomek(-7, 5))', '-7/5'),
                    ('str(Ulomek(7, -5))', '-7/5'),
                    ('str(Ulomek(-7, -5))', '7/5'),
                    ('str(Ulomek(20, 6))', '10/3'),
                    ('str(Ulomek(40, -60))', '-2/3')
                    ]
            
            for test in tests:
                if not Check.equal(*test):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoyMTA0MH0:1hR9zk:NPPTzWWjFQmXX4c_XhAYFTu0OLM'
        try:
            tests = [
                    ('repr(Ulomek(20, 6))', 'Ulomek(10, 3)'),
                    ('repr(Ulomek(0, 226))', 'Ulomek(0, 1)'),
                    ('repr(Ulomek(40, -60))', 'Ulomek(-2, 3)'),
                    ('repr(Ulomek(5, 20))', 'Ulomek(1, 4)'),
                    ('repr(Ulomek(5, 7))', 'Ulomek(5, 7)'),
                    ('repr(Ulomek(7, 5))', 'Ulomek(7, 5)'),
                    ('repr(Ulomek(-7, 5))', 'Ulomek(-7, 5)'),
                    ('repr(Ulomek(7, -5))', 'Ulomek(-7, 5)'),
                    ('repr(Ulomek(-7, -5))', 'Ulomek(7, 5)')
                    ]
            
            for test in tests:
                if not Check.equal(*test):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoyMTA0MX0:1hR9zk:N_0c38twBQzidtXCl3uek6NeHeY'
        try:
            tests = [
                    ('Ulomek(1, 3) == Ulomek(2, 3)', False),
                    ('Ulomek(2, 3) == Ulomek(10, 15)', True),
                    ('Ulomek(0, 3) == Ulomek(0, 2215)', True),
                    ('Ulomek(20, 6) == Ulomek(10, 3)', True),
                    ('Ulomek(-10, 3) == Ulomek(10, 3)', False),
                    ('Ulomek(10, -3) == Ulomek(10, 3)', False),
                    ('Ulomek(1, 4) == Ulomek(4, 1)', False),
                    ('Ulomek(20, 6) == Ulomek(10, 3)', True),
                    ('Ulomek(40, -60) == Ulomek(-2, 3)', True),
                    ('Ulomek(5, 20) == Ulomek(1, 4)', True),
                    ('Ulomek(5, 7) == Ulomek(5, 7)', True),
                    ('Ulomek(7, 5) == Ulomek(7, 5)', True),
                    ('Ulomek(-7, 5) == Ulomek(-7, 5)', True),
                    ('Ulomek(7, -5) == Ulomek(-7, 5)', True),
                    ('Ulomek(-7, -5) == Ulomek(7, 5)', True),
                    ('Ulomek(999999999, 1000000000) == Ulomek(999999998, 999999999)', False),
                    ('Ulomek(20, 6) == Ulomek(10, 3)', True),
                    ('Ulomek(-10, 3) == Ulomek(10, 3)', False),
                    ('Ulomek(1, 4) == Ulomek(4, 1)', False)
                    ]
            
            for test in tests:
                if not Check.equal(*test):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoyMTA0Mn0:1hR9zk:dWPRBwSEkk23PjJw4I1CJ2CTmOk'
        try:
            tests = [
                    ('Ulomek(1, 6) + Ulomek(1, 4)', Ulomek(5, 12)),
                    ('Ulomek(1, 6) + Ulomek(1, 6)', Ulomek(1, 3)),
                    ('Ulomek(1, 6) + Ulomek(1, 4)', Ulomek(5, 12)),
                    ('Ulomek(1, -6) + Ulomek(-1, 4)', Ulomek(-5, 12)),
                    ('Ulomek(1, 6) + Ulomek(-1, 4)', Ulomek(-1, 12)),
                    ('Ulomek(1, -6) + Ulomek(1, 4)', Ulomek(1, 12)),
                    ('Ulomek(1, 6) + Ulomek(1, 6)', Ulomek(1, 3)),
                    ('Ulomek(1, 6) + Ulomek(-1, 6)', Ulomek(0, 1)),
                    ('Ulomek(60, 1) + Ulomek(-1, 60)', Ulomek(3599, 60)),
                    ('Ulomek(1, 2014) + Ulomek(1, 2015)', Ulomek(4029, 4058210)),
                    ('Ulomek(1, 2014) + Ulomek(1, -2015)', Ulomek(1, 4058210)),
                    ('Ulomek(757, 3000) + Ulomek(743, 3000)', Ulomek(1, 2)),
                    ('Ulomek(1009, 2022) + Ulomek(1013, 2022)', Ulomek(1, 1))
                    ]
            
            for test in tests:
                if not Check.equal(*test):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoyMTA0M30:1hR9zk:7rJhqlscSgon1vKCSB9PnQ53SLU'
        try:
            tests = [
                    ('Ulomek(1, 6) - Ulomek(1, 4)', Ulomek(-1, 12)),
                    ('Ulomek(3, 6) - Ulomek(1, 6)', Ulomek(1, 3)),
                    ('Ulomek(1, 6) - Ulomek(1, 4)', Ulomek(-1, 12)),
                    ('Ulomek(1, 4) - Ulomek(1, 6)', Ulomek(1, 12)),
                    ('Ulomek(3, 6) - Ulomek(1, 6)', Ulomek(1, 3)),
                    ('Ulomek(1, -6) - Ulomek(-1, 4)', Ulomek(1, 12)),
                    ('Ulomek(1, 6) - Ulomek(-1, 4)', Ulomek(5, 12)),
                    ('Ulomek(1, -6) - Ulomek(1, 4)', Ulomek(-5, 12)),
                    ('Ulomek(1, 6) - Ulomek(1, 6)', Ulomek(0, 1)),
                    ('Ulomek(1, 6) - Ulomek(-1, 6)', Ulomek(1, 3)),
                    ('Ulomek(60, 1) - Ulomek(-1, 60)', Ulomek(3601, 60)),
                    ('Ulomek(1, 2014) - Ulomek(1, 2015)', Ulomek(1, 4058210)),
                    ('Ulomek(1, 2014) - Ulomek(1, -2015)', Ulomek(4029, 4058210)),
                    ('Ulomek(757, 3000) - Ulomek(743, 3000)', Ulomek(7, 1500)),
                    ('Ulomek(2003, 1980) - Ulomek(1013, 1980)', Ulomek(1, 2))
                    ]
            
            for test in tests:
                if not Check.equal(*test):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoyMTA0NH0:1hR9zk:vt5GatDl31jBphFJ6pXLhB5TxCQ'
        try:
            tests = [
                    ('Ulomek(1, 6) * Ulomek(1, 4)', Ulomek(1, 24)),
                    ('Ulomek(4, 9) * Ulomek(3, 2)', Ulomek(2, 3)),
                    ('Ulomek(1, 3) * Ulomek(1, 2)', Ulomek(1, 6)),
                    ('Ulomek(1, 6) * Ulomek(1, 4)', Ulomek(1, 24)),
                    ('Ulomek(4, 9) * Ulomek(3, 2)', Ulomek(2, 3)),
                    ('Ulomek(1, -6) * Ulomek(-1, 4)', Ulomek(1, 24)),
                    ('Ulomek(1, 6) * Ulomek(-1, 4)', Ulomek(-1, 24)),
                    ('Ulomek(1, -6) * Ulomek(1, 4)', Ulomek(-1, 24)),
                    ('Ulomek(757, 3000) * Ulomek(743, 3000)', Ulomek(562451, 9000000)),
                    ('Ulomek(60, 1) * Ulomek(-1, 60)', Ulomek(-1, 1)),
                    ('Ulomek(25857, 160930) * Ulomek(277970, 33813)', Ulomek(247, 187)),
                    ('Ulomek(25857, 1) * Ulomek(277970, 1)', Ulomek(7187470290, 1))
                    ]
            
            for test in tests:
                if not Check.equal(*test):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoyMTA0NX0:1hR9zk:RldeOPPIZ2qknr1JJsKqBzm0rx0'
        try:
            tests = [
                    ('Ulomek(1, 6) / Ulomek(1, 4)', Ulomek(2, 3)),
                    ('Ulomek(4, 9) / Ulomek(2, 3)', Ulomek(2, 3)),
                    ('Ulomek(1, -6) / Ulomek(-1, 4)', Ulomek(2, 3)),
                    ('Ulomek(1, 6) / Ulomek(-1, 4)', Ulomek(-2, 3)),
                    ('Ulomek(1, -6) / Ulomek(1, 4)', Ulomek(-2, 3)),
                    ('Ulomek(757, 3000) / Ulomek(743, 3000)', Ulomek(757, 743)),
                    ('Ulomek(757, 3000) / Ulomek(3000, 743)', Ulomek(562451, 9000000)),
                    ('Ulomek(60, 1) / Ulomek(-60, 1)', Ulomek(-1, 1)),
                    ('Ulomek(160930, 25857) / Ulomek(277970, 33813)', Ulomek(187, 247)),
                    ('Ulomek(25857, 1) / Ulomek(277970, 1)', Ulomek(25857, 277970)),
                    ('Ulomek(25857, 1) / Ulomek(1, 277970)', Ulomek(7187470290, 1)),
                    ('Ulomek(1, 6) / Ulomek(1, 4)', Ulomek(2, 3)),
                    ('Ulomek(4, 9) / Ulomek(2, 3)', Ulomek(2, 3))
                    ]
            
            for test in tests:
                if not Check.equal(*test):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoyMTA0Nn0:1hR9zk:BxVywrkpXJZs_nq-BPelWublszc'
        try:
            tests = [
                    ('priblizek(3)', Ulomek(8, 3)),
                    ('priblizek(5)', Ulomek(163, 60)),
                    ('priblizek(10)', Ulomek(9864101, 3628800)),
                    ('priblizek(3)', Ulomek(8, 3)),
                    ('priblizek(1)', Ulomek(2, 1)),
                    ('priblizek(0)', Ulomek(1, 1)),
                    ('priblizek(5)', Ulomek(163, 60)),
                    ('priblizek(10)', Ulomek(9864101, 3628800))
                    ]
            
            for test in tests:
                if not Check.equal(*test):
                    break
                    
            Check.equal('priblizek(20)', Ulomek(6613313319248080001, 2432902008176640000)) or \
            Check.equal('round(eval(str(priblizek(20))),5)', round(eval(str(Ulomek(6613313319248080001, 2432902008176640000)))),5)
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
