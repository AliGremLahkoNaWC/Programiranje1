# =============================================================================
# Ednina, dvojina, množina
# =====================================================================@017296=
# 1. podnaloga
# Napiši funkcijo `finStanje(n)`, ki kot argument sprejme količino denarja
# na bančnem računu, podano v evrih (celih) in slovničnemu številu
# ustrezno vrne opis finančnega stanja.
# 
#      >>>finStanje(1)
#      Stanje: 1 evro.
#      >>>finStanje(1002)
#      Stanje: 1002 evra.
#      >>>finStanje(-203)
#      Stanje: -203 evri.
#      >>>finStanje(215)
#      Stanje: 215 evrov.
# 
# Primer, če je vneseno stanje večje ali enako 1000000 evrov:
# 
#      >>>finStanje(1000002)
#      Tajkun!
# 
# Primer, če je vneseno stanje nižje od -300 evrov: 
# 
#      >>>finStanje(-302)
#      Ti si navadna zguba!
# =============================================================================

def finStanje(n):
    '''
    Funkcija bo povedala finančno stanje glede na vnešeno količino
    '''
    if n >= 1000000:
        return ("Tajkun!")
    if n < -300:
        return ("Ti si navadna zguba!")
    if n >= 0:
        if n == 0 or (n % 10 == 3 and (n // 10) > 10):
            return ("Stanje: {} evrov." .format(n))
        if n == 1 or n % 10 == 1:
            return ("Stanje: {} evro." .format(n))
        if n == 2 or n % 10 == 2 and (n // 10) > 10:
            return ("Stanje: {} evra." .format(n))
        if n == 3 or n % 10 == 3:
            return ("Stanje: {} evri." .format(n))
        else:
            return ("Stanje: {} evrov." .format(n))
    if n < 0:
        if ((n * -1) % 10 == 3 and ((n * -1) // 10) > 10):
            return ("Stanje: {} evrov." .format(n))
        if n == -1 or (n * -1) % 10 == 1:
            return ("Stanje: {} evro." .format(n))
        if n == -2 or (n * -1) % 10 == 2:
            return ("Stanje: {} evra." .format(n))
        if n == -3 or (n * -1) % 10 == 3 or n == -4 or (n * -1) % 10 == 4:
            return ("Stanje: {} evri." .format(n))
        else:
            return ("Stanje: {} evrov." .format(n))
# =====================================================================@017297=
# 2. podnaloga
# Sestavi funkcijo `stLjudi(n)`, ki kot argument sprejme poljubno naravno
# število in nato v slovnično pravilni obliki vrne opis števila ljudi
# v dvorani kulturnega doma (glej zglede). Dvorana sprejme največ 500 ljudi. Podatki so smiselni, torej
# celo število, večje ali enako 0.
# Primer za n=0:
# 
#      Dvorana je prazna.
# 
# Primer za n=1:
# 
#      V dvorani je 1 človek.
# 
# Primer za n=303:
# 
#      V dvorani so 303 ljudje.
# 
# Primer za n=500:
# 
#      Dvorana je polna.
# 
# Primer za n=502:
# 
#      Dvorana je polna. Zunaj sta ostala 2 človeka.
# =============================================================================

def stLjudi(n):
    '''
    Funkcija bo povedala stanje okupiranosti dvorane.
    '''
    if n <= 500:
        if n == 0:
            return ("Dvorana je prazna.")
        if n == 500:
            return ("Dvorana je polna.")
        if n % 10 == 1:
            return ("V dvorani je {} človek." .format(n))
        if n == 2 or n % 10 == 2:
            return ("V dvorani sta {} človeka." .format(n))
        if (n == 3 or n == 4) or (n % 10 == 3 or n % 10 == 4):
            return ("V dvorani so {} ljudje." .format(n))
        else:
            return ("V dvorani je {} ljudi." .format(n))
    elif n > 500:
        ostanek = n - 500
        if ostanek == 1 or ostanek % 10 == 1:
            return ("Dvorana je polna. Zunaj je ostal {} človek." .format(ostanek))
        if ostanek == 2 or ostanek % 10 == 2:
            return ("Dvorana je polna. Zunaj sta ostala {} človeka." .format(ostanek))
        if (ostanek == 3 or ostanek == 4) or (ostanek % 10 == 3 or ostanek % 10 == 4):
            return ("Dvorana je polna. Zunaj so ostali {} ljudje." .format(ostanek))
        else:
            return ("Dvorana je polna. Zunaj je ostalo {} ljudi." .format(ostanek))
            
        
# =====================================================================@017298=
# 3. podnaloga
# Sestavite program, ki prebere naravno število `n` in nato izpiše niz oblike
# 
#     Koliko imaš limon: 103
#     Imaš 103 limone.
#     Koliko imaš limon: 0
#     Imaš 0 limon.
# 
# pri čemer mora biti seveda vse pravilno sklanjano.
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
                errors.append('nastavijo {0} na {1!r} namesto na {2!r}'.format(x, s[x], v))
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
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoxNzI5Nn0:1gH1ra:bn3Acgh9AHgkE7I66UI-bTbE5Ew'
        try:
            Check.equal("finStanje(0)", 'Stanje: 0 evrov.') and  \
            Check.equal("finStanje(1)", 'Stanje: 1 evro.') and  \
            Check.equal("finStanje(2)", 'Stanje: 2 evra.') and  \
            Check.equal("finStanje(3)", 'Stanje: 3 evri.') and  \
            Check.equal("finStanje(103)", 'Stanje: 103 evri.') and  \
            Check.equal("finStanje(113)", 'Stanje: 113 evrov.') and  \
            Check.equal("finStanje(-3)", 'Stanje: -3 evri.') and  \
            Check.equal("finStanje(-4)", 'Stanje: -4 evri.') and  \
            Check.equal("finStanje(-5)", 'Stanje: -5 evrov.') and  \
            Check.equal("finStanje(-300)", 'Stanje: -300 evrov.') and  \
            Check.equal("finStanje(-101)", 'Stanje: -101 evro.') and  \
            Check.equal("finStanje(202)", 'Stanje: 202 evra.') and  \
            Check.equal("finStanje(222)", 'Stanje: 222 evrov.') and  \
            Check.equal("finStanje(16232)", 'Stanje: 16232 evrov.') and  \
            Check.equal("finStanje(404)", 'Stanje: 404 evri.') and  \
            Check.equal("finStanje(555)", 'Stanje: 555 evrov.') and  \
            Check.equal("finStanje(1000000)", 'Tajkun!') and  \
            Check.equal("finStanje(1010000)", 'Tajkun!') and  \
            Check.equal("finStanje(999999)", 'Stanje: 999999 evrov.') and  \
            Check.equal("finStanje(-300)", 'Stanje: -300 evrov.') and  \
            Check.equal("finStanje(-301)", 'Ti si navadna zguba!') and  \
            Check.equal("finStanje(-30108)", 'Ti si navadna zguba!')
            Check.secret("""finStanje(30108)""")
            Check.secret("""finStanje(1081)""")
            Check.secret("""finStanje(-108)""")
            Check.secret("""finStanje(1083)""")
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoxNzI5N30:1gH1ra:7g6yFGY7H3j56Zzko0fG6QPZnfs'
        try:
            Check.equal("stLjudi(0)", 'Dvorana je prazna.') and \
            Check.equal("stLjudi(1)",'V dvorani je 1 človek.') and \
            Check.equal("stLjudi(2)",'V dvorani sta 2 človeka.') and \
            Check.equal("stLjudi(3)",'V dvorani so 3 ljudje.') and \
            Check.equal("stLjudi(4)",'V dvorani so 4 ljudje.') and \
            Check.equal("stLjudi(5)",'V dvorani je 5 ljudi.') and \
            Check.equal("stLjudi(10)",'V dvorani je 10 ljudi.') and \
            Check.equal("stLjudi(101)",'V dvorani je 101 človek.') and \
            Check.equal("stLjudi(202)",'V dvorani sta 202 človeka.') and \
            Check.equal("stLjudi(303)",'V dvorani so 303 ljudje.') and \
            Check.equal("stLjudi(404)",'V dvorani so 404 ljudje.') and \
            Check.equal("stLjudi(499)",'V dvorani je 499 ljudi.') and \
            Check.equal("stLjudi(500)",'Dvorana je polna.') and \
            Check.equal("stLjudi(501)",'Dvorana je polna. Zunaj je ostal 1 človek.') and \
            Check.equal("stLjudi(602)",'Dvorana je polna. Zunaj sta ostala 102 človeka.') and \
            Check.equal("stLjudi(703)",'Dvorana je polna. Zunaj so ostali 203 ljudje.') and \
            Check.equal("stLjudi(804)",'Dvorana je polna. Zunaj so ostali 304 ljudje.') and \
            Check.equal("stLjudi(905)",'Dvorana je polna. Zunaj je ostalo 405 ljudi.')
            Check.secret("""stLjudi(30108)""")
            Check.secret("""stLjudi(11)""")
            Check.secret("""stLjudi(108)""")
            Check.secret("""stLjudi(1083)""")
            Check.secret("""stLjudi(81)""")
            Check.secret("""stLjudi(108)""")
            Check.secret("""stLjudi(102)""")
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoxNzI5OH0:1gH1ra:ecnuRHTfpaaPhp5x0uI4f0D8lEM'
        try:
            vhod = ['14', '101', '4', '202', '7', '1267', '303', '23', '111']
            izhod = ['', 'o', 'e', 'i', '', '', 'e', '', '']
            
            for i in range(len(vhod)):
                with Check.input([vhod[i]]):
                    if not Check.output(Check.current_part['solution'], [
                        'Koliko imaš limon: ' + vhod[i],
                        "Imaš {0} limon{1}.".format(vhod[i], izhod[i]),
                        ]):
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
