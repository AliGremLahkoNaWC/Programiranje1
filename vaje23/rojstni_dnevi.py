# =============================================================================
# Rojstni dnevi
#
# Tone ima slab spomin in si ne more zapomniti, kdaj ima kak njegov znanec
# rojstni dan. Zato si je podatke zapisal v datoteko, in sicer v naslednji
# obliki: v vsaki vrstici najprej navede ime osebe, nato priimek, nato dan
# (podan s številom, za katerim je pika) in na koncu ime meseca. Vsi ti deli so
# ločeni s po enim presledkom. Tone je natančen in se strogo drži teh pravil: v
# njegovi datoteki ni tipkarskih napak in vsaka oseba je podana samo z imenom
# in priimkom (brez srednjih imen itd.).
# 
# Kot primer bomo vzeli datoteko po imenu `rojstni_dnevi.txt`, katere vsebina
# izgleda takole:
# 
#     Mojca Vrstnik 2. december
#     Ivan Sotomajer 15. maj
#     Jan Nebuša 29. februar
#     Iljana Potrebuješ 15. maj
#     Beg Krigelj 18. september
# 
# Seveda Tone ne želi vsakodnevno lastnoročno odpirati in pregledovati
# datoteke, pač pa želi bolj udoben način opominjanja na rojstne dneve. Ker ve,
# da se vi spoznate na programiranje, vas je zaprosil za pomoč.
# =====================================================================@019584=
# 1. podnaloga
# Sestavite funkcijo `slovar_rojstnih_dni(datoteka)`, ki sprejme ime datoteke,
# zapisane v obliki kot je prikazano zgoraj, in vrne slovar. Ključi slovarja naj
# bodo polna imena oseb (tj. ime in priimek skupaj, ločena s presledkom),
# vrednosti pa naj bodo številski pari, kjer prvo število predstavlja dan,
# drugo pa zaporedno število meseca rojstnega dneva.
# 
#     >>> slovar_rojstnih_dni('rojstni_dnevi.txt')
#     {'Beg Krigelj': (18, 9), 'Mojca Vrstnik': (2, 12), 'Iljana Potrebuješ': (15, 5),
#       'Jan Nebuša': (29, 2), 'Ivan Sotomajer': (15, 5)}
# 
# V pomoč sta vam lahko sledeča nabor in slovar, s katerima lahko enostavno
# pretvarjate med meseci, danimi s števili, in meseci, danimi z imeni.
# 
#     imena_mesecev = ('januar', 'februar', 'marec', 'april', 'maj', 'junij',
#                      'julij', 'avgust', 'september', 'oktober', 'november', 'december')
#     meseci = {mesec: stevilo + 1 for stevilo, mesec in enumerate(imena_mesecev)}
# =============================================================================
imena_mesecev = ('januar', 'februar', 'marec', 'april', 'maj', 'junij',
                'julij', 'avgust', 'september', 'oktober', 'november', 'december')
meseci = {mesec: stevilo + 1 for stevilo, mesec in enumerate(imena_mesecev)}
print(meseci)
def slovar_rojstnih_dni(datoteka):
    '''funkcija sprejme datoteko in vrne slovar'''
    slovar = dict()
    
    for vrstica in open(datoteka, 'r'):
        vrstica = vrstica.strip().split('.')
        ime, datum = vrstica[0].split(), vrstica[1].strip()
        niz = ime[0] + ' ' + ime[1]
        slovar[niz] = (int(ime[2]), int(meseci[datum]))
    return slovar
# =====================================================================@019585=
# 2. podnaloga
# Sestavite funkcijo `praznovalci(datoteka, dan, mesec)`, ki (glede na podatke
# iz podane datoteke) vrne množico vseh oseb, ki imajo rojstni dan na dani
# datum. Pri tem je `dan` podan kot število, `mesec` pa bodisi kot število
# bodisi kot ime meseca. Če na dani datum nihče nima rojstnega dne, naj program
# seveda vrne prazno množico.
# 
#     >>> praznovalci('rojstni_dnevi.txt', 2, 12)
#     {'Mojca Vrstnik'}
#     >>> praznovalci('rojstni_dnevi.txt', 15, 'maj')
#     {'Iljana Potrebuješ', 'Ivan Sotomajer'}
#     >>> praznovalci('rojstni_dnevi.txt', 1, 'januar')
#     set()
# =============================================================================

# =====================================================================@019586=
# 3. podnaloga
# Sestavite funkcijo `naslednji_rojstni_dan(datoteka, dan, mesec)`, ki pri danem
# datumu (podanemu, kot v prejšnji podnalogi) vrne prvi datum po njem (ali enak
# njemu), ko ima kdo rojstni dan (morebiti šele naslednje leto), ter zraven
# poda še množico oseb, ki imajo takrat rojstni dan. Natančneje, rezultat naj
# bo nabor, katerega prvi element je datum, podan kot niz oblike
# 'dan. ime meseca', drugi element pa je množica praznovalcev. Predpostaviti
# smete, da datoteka ni prazna (tj. Tone ima vsaj enega znanca).
# 
#     >>> naslednji_rojstni_dan('rojstni_dnevi.txt', 1, 6)
#     ('18. september', {'Beg Krigelj'})
#     >>> naslednji_rojstni_dan('rojstni_dnevi.txt', 15, 'maj')
#     ('15. maj', {'Iljana Potrebuješ', 'Ivan Sotomajer'})
#     >>> naslednji_rojstni_dan('rojstni_dnevi.txt', 29, 'december')
#     ('29. februar', {'Jan Nebuša'})
# 
# Kot vidiš, je mesec lahko podan s številko ali besedo!
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
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoxOTU4NH0:1hOdYS:p6YXfKa47c1r7-w8MPt-dk50jmE'
        try:
            with open('rojstni_dnevi.txt', 'w') as f:
                print('Mojca Vrstnik 2. december', file=f)
                print('Ivan Sotomajer 15. maj', file=f)
                print('Jan Nebuša 29. februar', file=f)
                print('Iljana Potrebuješ 15. maj', file=f)
                print('Beg Krigelj 18. september', file=f)
            
            Check.equal("slovar_rojstnih_dni('rojstni_dnevi.txt')", {'Beg Krigelj': (18, 9), 'Mojca Vrstnik': (2, 12), 'Iljana Potrebuješ': (15, 5),
                                                                     'Jan Nebuša': (29, 2), 'Ivan Sotomajer': (15, 5)})
            
            with open('brez_prijateljev.txt', 'w') as f:
                pass
            Check.equal("slovar_rojstnih_dni('brez_prijateljev.txt')", dict())
            
            with open('rojstni_dnevi2.txt', 'w') as f:
                print('Mojca Vrstnik 2. december', file=f)
                print('Mojca Vrstni 2. december', file=f)
                print('Ivan Sotomajer 2. december', file=f)
                print('Jan Nebuša 29. februar', file=f)
                print('Iljana Potrebuješ 15. maj', file=f)
                print('Beg Krigelj 18. september', file=f)
            
            Check.equal("slovar_rojstnih_dni('rojstni_dnevi2.txt')", {'Beg Krigelj': (18, 9), 'Mojca Vrstnik': (2, 12), 'Mojca Vrstni': (2, 12),
                                                                      'Iljana Potrebuješ': (15, 5), 'Jan Nebuša': (29, 2), 'Ivan Sotomajer': (2, 12)})
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoxOTU4NX0:1hOdYS:LTyRk7Kb07E5-XtpmBTJtYcmQOk'
        try:
            tests = [
                    ("praznovalci('rojstni_dnevi2.txt', 2, 12)", {'Mojca Vrstnik', 'Mojca Vrstni', 'Ivan Sotomajer'}),
                    ("praznovalci('rojstni_dnevi.txt', 15, 'maj')", {'Iljana Potrebuješ', 'Ivan Sotomajer'}),
                    ("praznovalci('rojstni_dnevi.txt', 1, 'januar')", set()),
                    ("praznovalci('rojstni_dnevi.txt', 2, 12)", {'Mojca Vrstnik'}) ,
                    ("praznovalci('rojstni_dnevi2.txt', 15, 'maj')", {'Iljana Potrebuješ'}),
                    ("praznovalci('rojstni_dnevi2.txt', 1, 'januar')", set()),
                    ("praznovalci('brez_prijateljev.txt', 2, 12)", set()),
                    ("praznovalci('brez_prijateljev.txt', 15, 'maj')", set())
                    ]
            
            for test in tests:
                if not Check.equal(*test):
                    break
            
            for dan in range(1, 29):
                for mesec in range(1, 13):
                    Check.secret(praznovalci('rojstni_dnevi.txt', dan, mesec), 'Pri pregledu vseh prvih 28 dni vseh mesecev se tvoj program ni obnesel!')
            
            for dan in range(1, 29):
                for mesec in range(1, 13):
                    Check.secret(praznovalci('brez_prijateljev.txt', dan, mesec), 'Pri pregledu vseh prvih 28 dni vseh mesecev se tvoj program ni obnesel!')
                    
            for dan in range(1, 29):
                for mesec in range(1, 13):
                    Check.secret(praznovalci('rojstni_dnevi2.txt', dan, mesec), 'Pri pregledu vseh prvih 28 dni vseh mesecev se tvoj program ni obnesel!')
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoxOTU4Nn0:1hOdYS:xvbQVUgbLxKeFmUmV6Dzr0pehj4'
        try:
            tests = [
                    ("naslednji_rojstni_dan('rojstni_dnevi.txt', 1, 6)", ('18. september', {'Beg Krigelj'})),
                    ("naslednji_rojstni_dan('rojstni_dnevi.txt', 17, 'september')", ('18. september', {'Beg Krigelj'})),
                    ("naslednji_rojstni_dan('rojstni_dnevi.txt', 15, 5)", ('15. maj', {'Iljana Potrebuješ', 'Ivan Sotomajer'})),
                    ("naslednji_rojstni_dan('rojstni_dnevi.txt', 15, 'maj')", ('15. maj', {'Iljana Potrebuješ', 'Ivan Sotomajer'})),
                    ("naslednji_rojstni_dan('rojstni_dnevi.txt', 29, 'december')", ('29. februar', {'Jan Nebuša'}))
                    ]
            
            for test in tests:
                if not Check.equal(*test):
                    break
            
            for dan in range(1, 29):
                for mesec in range(1, 13):
                    Check.secret(naslednji_rojstni_dan('rojstni_dnevi.txt', dan, mesec),
                                 'Pri pregledu vseh prvih 28 dni vseh mesecev se tvoja funkcija ni obnesla za vsaj en datum!')
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
