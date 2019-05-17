# =============================================================================
# Mere
# =====================================================================@021067=
# 1. podnaloga
# Sestavi razred `Dolzina`. Najprej sestavi konstruktor 
# `__init__(self, st, enota)`, ki sprejme stevilo (dolzino) in enoto, v kateri
# je dolzina podana (mm, cm, dm, m ali km).
# Konstruktor naj preveri, ali je dano stevilo veljavna dolzina (nenegativno) in
# če ni, naj vrne napako. Premisli, na kakšen način bi bilo najbolje shraniti
# podatke.
# 
# Ta podnaloga nima testnih primerov.
# =============================================================================
class Dolzina:

    def __init__(self, st, enota):
        if st < 0:
            raise ValueError('Dolzina je lahko le nenegativna!')
        enote = ('mm', 'cm', 'dm', 'm', 'km')
        if enota not in enote:
            raise ('Podana enota ne obstaja')
        self.stevilo = st
        self.mera = str(enota)
        
# =====================================================================@021068=
# 2. podnaloga
# Sestavi metodo `get(self, enota)`, ki sprejme enoto, v kateri naj bo rezultat
# podan, rezultat pa naj bo oblike (stevilo, enota).
# 
# Primer:
# 
#     >>> Dolzina(2500, "cm").get("dm")
#     (250, "dm")
# =============================================================================
class Dolzina(Dolzina):

    def get(self, enota):
        pretvorba = {'km': 1, 'm': 1000, 'dm': 10000, 'cm': 100000, 'mm': 1000000}
        if self.mera == enota:
            return (self.stevilo, self.mera)
        if pretvorba[self.mera] < pretvorba[enota]:
            return (self.stevilo*(pretvorba[enota]//pretvorba[self.mera]), enota)
        else:
            return (self.stevilo/(pretvorba[self.mera]//pretvorba[enota]), enota)
# =====================================================================@021069=
# 3. podnaloga
# Sestavi metodo `__add__`, ki sešteje dve dolžini. Če desni operant ni objekt
# razreda `Dolzina`, naj metoda vrne napako.
# 
# Primer:
# 
#     >>> d = Dolzina(2500, "cm") + Dolzina(2500, "mm")
#     >>> d.get("mm")
#     (27500, "mm")
# =============================================================================
class Dolzina(Dolzina):

    def __add__(self, other):
        if self.mera != other.mera:
            d = Dolzina(self.stevilo, self.mera).get(other.mera)
            return Dolzina(d[0] + other.stevilo, other.mera)
        else:
            return Dolzina(self.stevilo + other.stevilo, self.mera)
# =====================================================================@021070=
# 4. podnaloga
# Sestavi metodo `__mul__`, ki zmnoži dolžino z danim skalarjem z desne strani.
# Kako se metoda spremeni, če želimo množiti s skalarjem z leve strani?
# 
# Primer:
# 
#     >>> d = Dolzina(2500, "cm") * 5
#     >>> d.get("mm")
#     (125000, "mm")
# =============================================================================
class Dolzina(Dolzina):

    def __mul__(self, skalar):
        d = Dolzina(self.stevilo * skalar, self.mera)
        return d
# =====================================================================@021071=
# 5. podnaloga
# Metodo `__mul__` dopolni tako, da omogočila množenje dveh dolžin. Rezultat naj
# bo objekt razreda Ploscina, ki naj vsebuje konstrutor 
# `__init__(self, velikost)` in metodo `get(self, enota)`. Konstruktor naj
# dovoli shranjevanje velikosti le v mm**2, metoda get pa naj, tako kot v razredu
# Dolzina, enoto, v kateri naj bo rezultat, sprejme kot parameter. Enote naj
# bodo izpisane v obliki `mm**2, cm**2, dm**2, m**2, km**2`.
# 
# Primer:
# 
#     >>> d = Dolzina(2500, "cm") * Dolzina(30, "mm")
#     >>> d.get("dm**2")
#     (75, "dm**2")
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
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoyMTA2N30:1hRet2:gTIHVeYQJvnj-BsEamsyXpaiC_w'
        try:
            pass
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoyMTA2OH0:1hRet2:ldz47W1L-XiJj395l1kQfI0YyzY'
        try:
            tests = [
                    ('Dolzina(2500, "mm").get("mm")', (2500, "mm")),
                    ('Dolzina(2500, "cm").get("dm")', (250, "dm")),
                    ('Dolzina(2500, "dm").get("km")', (0.25, "km")),
                    ('Dolzina(2500, "m").get("cm")', (250000, "cm")),
                    ('Dolzina(2500, "km").get("m")', (2500000, "m")),
                    ('Dolzina(2500, "mm").get("km")', (0.0025, "km")),
                    ('Dolzina(2500, "cm").get("m")', (25, "m")),
                    ('Dolzina(2500, "dm").get("dm")', (2500, "dm")),
                    ('Dolzina(2500, "m").get("mm")', (2500000, "mm")),
                    ('Dolzina(2500, "km").get("cm")', (250000000, "cm")),
                    ('Dolzina(0, "km").get("cm")', (0, "cm"))
                    ]
            
            for test in tests:
                if not Check.equal(*test):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoyMTA2OX0:1hRet2:Yw66q9pZarYW7VK1EaldOizgANw'
        try:
            tests = [
                    ('( Dolzina(2500, "mm") + Dolzina(2500, "mm") ).get("mm")', (5000, "mm")),
                    ('( Dolzina(2500, "cm") + Dolzina(2500, "mm") ).get("mm")', (27500, "mm")),
                    ('( Dolzina(2500, "dm") + Dolzina(2500, "m") ).get("mm")', (2750000, "mm")),
                    ('( Dolzina(2500, "m") + Dolzina(0, "mm") ).get("mm")', (2500000, "mm")),
                    ('( Dolzina(2500, "km") + Dolzina(250, "m") ).get("mm")', (2500250000, "mm")),
                    ('( Dolzina(2500, "mm") + Dolzina(250, "dm") ).get("mm")', (27500, "mm")),
                    ('( Dolzina(2500, "cm") + Dolzina(250, "dm") ).get("mm")', (50000, "mm")),
                    ('( Dolzina(2500, "dm") + Dolzina(250, "km") ).get("mm")', (250250000, "mm")),
                    ('( Dolzina(2500, "m") + Dolzina(250, "cm") ).get("mm")', (2502500, "mm")),
                    ('( Dolzina(2500, "km") + Dolzina(250, "mm") ).get("mm")', (2500000250, "mm")),
                    ('( Dolzina(0, "km") + Dolzina(250, "cm") ).get("mm")', (2500, "mm"))
                    ]
            
            for test in tests:
                if not Check.equal(*test):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoyMTA3MH0:1hRet2:Sw3Be_UbNba_7H8GvJW1JW8lgTg'
        try:
            tests = [
                    ('( Dolzina(2500, "mm") * 4 ).get("mm")', (10000, "mm")),
                    ('( Dolzina(2500, "cm") * 5 ).get("mm")', (125000, "mm")),
                    ('( Dolzina(2500, "dm") * 6 ).get("mm")', (1500000, "mm")),
                    ('( Dolzina(2500, "m") * 0 ).get("mm")', (0, "mm")),
                    ('( Dolzina(2500, "km") * 0.5 ).get("mm")', (1250000000, "mm")),
                    ('( Dolzina(2500, "mm") * 0.25 ).get("mm")', (625, "mm")),
                    ('( Dolzina(2500, "cm") * 25 ).get("mm")', (625000, "mm")),
                    ('( Dolzina(2500, "dm") * 100 ).get("mm")', (25000000, "mm")),
                    ('( Dolzina(2500, "m") * 500 ).get("mm")', (1250000000, "mm")),
                    ('( Dolzina(2500, "km") * 75 ).get("mm")', (187500000000, "mm")),
                    ('( Dolzina(0, "km") * 125 ).get("mm")', (0, "mm"))
                    ]
            
            for test in tests:
                if not Check.equal(*test):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoyMTA3MX0:1hRet2:Js3V_lTEpNrjebcjiaF_-9UUk6A'
        try:
            tests = [
                    ('( Dolzina(2500, "mm") * 4 ).get("mm")', (10000, "mm")),
                    ('( Dolzina(2500, "cm") * 5 ).get("mm")', (125000, "mm")),
                    ('( Dolzina(2500, "dm") * 6 ).get("mm")', (1500000, "mm")),
                    ('( Dolzina(2500, "m") * 0 ).get("mm")', (0, "mm")),
                    ('( Dolzina(2500, "km") * Dolzina(10, "mm")).get("mm**2")', (25000000000, "mm**2")),
                    ('( Dolzina(2500, "mm") * Dolzina(20, "mm") ).get("cm**2")', (500, "cm**2")),
                    ('( Dolzina(2500, "cm") * Dolzina(30, "mm") ).get("dm**2")', (75, "dm**2")),
                    ('( Dolzina(2500, "dm") * Dolzina(40, "mm") ).get("m**2")', (10, "m**2")),
                    ('( Dolzina(2500, "m") * Dolzina(50, "mm") ).get("mm**2")', (125000000, "mm**2")),
                    ('( Dolzina(2500, "km") * Dolzina(60, "mm") ).get("km**2")', (0.15, "km**2")),
                    ('( Dolzina(0, "km") * Dolzina(100, "mm") ).get("mm**2")', (0, "mm**2"))
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
