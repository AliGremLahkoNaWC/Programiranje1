# =============================================================================
# Hitri prsti
#
# Če na začetek programa napišemo
# 
#       import time
# 
# bomo, med drugim, dobili funkcijo `time`, ki s klicem `time.time()` vrne čas v sekundah
# od nekega trenutka v davni preteklosti.
# 
# **Pozor:** preverjanje lahko traja kar nekaj èasa - tudi do 20 sekund!
# =====================================================================@017316=
# 1. podnaloga
# **Kako hitro razmišljamo**
# 
# Napiši program, ki uporabnika vpraša, koliko je `a` krat `b`. Pri tem racunalnik generira
# `a` in`b` kot dve naključni enomestni naravni števili (vključno z 0).
# Uporabnik bo premislil in vpisal odgovor.
# Program naj izpiše, koliko sekund je človek potreboval za razmišljanje, ter, če je odgovor pravilen.
# Namig: če veš, koliko je bila ura pred klicem funkcije input in koliko je bila ura po klicu,
# znaš izračunati, koliko časa je minilo vmes.
# 
#     >>>Koliko je 6 x 7: 42
#     Čestitam! Odgovor je pravilen. Za odgovor si potreboval 2.503019332885742 s.
# 
#     >>>Koliko je 6 x 7: 40
#     Čestitam! Žal narobe! Prav je 42! Za odgovor si potreboval 2.503019332885742 s.
# =============================================================================
'''Program bo ocenil hitrost nasega mnozenja. '''
import time
import random
cas_zacetek = time.time()
a = random.randint(0,9)
b = random.randint(0,9)
odg = int(input("Koliko je {} krat {}: " .format(a,b)))
cas_konec = time.time()
rez = a * b
if odg == rez:
    print("Čestitam! Odgovor je pravilen. Za odgovor si potreboval {} s." .format(cas_konec))
else:
    print("Čestitam! Žal narobe! Prav je {}! Za odgovor si potreboval {} s." .format(rez,cas_konec))
# =====================================================================@017317=
# 2. podnaloga
# **Misleči stroj I**
# 
# Oglej si, kaj počne naslednji program:
# 
#     import time
# 
#     a = int(input('Prvo število: '))
#     b = int(input('Drugo število: '))
#     print('Računam ...')
#     time.sleep(3)
#     print('Uf, je bilo težko. V 3 sek so se moji čipi pošteno ogreli. Rezultat je:', a*b)
# 
# nato ga spremeni tako, da bo računalnik razmišljal med 1 in 5 sekundami!
# Pri tem lahko čaka tudi npr. 4.371232 sekunde ali pa točno 5! Oglej
# si [dokumentacijo](https://docs.python.org/3.5/library/random.html) in
# poišči ustrezno funkcijo. Čas razmišljanja izpiši zaokroženo na tisočinke!
# =============================================================================
import time
import random

a = int(input('Prvo število: '))
b = int(input('Drugo število: '))
print('Računam ...')
calc_time = round(random.uniform(1,5),3)
time.sleep(calc_time)
print('Uf, je bilo težko. V {} sek so se moji čipi pošteno ogreli. Rezultat je: {}' .format(calc_time,a*b))
# =====================================================================@017318=
# 3. podnaloga
# **Misleči stroj II**
# 
# Večji kot je produkt, težji je račun. Računalnik naj zato čaka toliko sekund, kolikor je velik produkt,
# deljeno z 10. Če mu damo množiti 6 in 7, naj pred
# izpisom počaka 4.2 sekunde.
# Če je katero od števil negativno, naj vedno čaka
# 2 sekundi več, kot bi čakal pri pozitivnih številih.
# V nobenem primeru pa čas čakanja ne sme biti več kot 10 sekund.
# 
# Izpis naj bo tak, kot ga predvideva zgornji program!
# =============================================================================
import time

a = int(input('Prvo število: '))
b = int(input('Drugo število: '))
print('Računam ...')


if (a or b) < 0:
    calc_time = abs((a * b) / 10) + 2    
else:
    calc_time = (a * b) / 10

if calc_time > 10:
    time.sleep(10)
else:
    time.sleep(calc_time)
   

print('Uf, je bilo težko. V {} sek so se moji čipi pošteno ogreli. Rezultat je: {}' .format(calc_time,a*b))




































































































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
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoxNzMxNn0:1gIsjW:r0S74DFmxT-nMoW5ne5eUmXVe3Q'
        try:
            import random
            koda = Check.current_part['solution']
            
            
            if 'time.time()' not in koda:
                Check.error("Čas meri s pomočju funkcije `time.time()`")
            
            elif not (('random.randint(0, 9)' in koda) or ('random.randint(0,9)' in koda) or ('random.randint(0 , 9)' in koda)):
                Check.error("Števili `a` in`b` morata biti dve naključni enomestni\nnaravni števili, vključno z 0!\nUporabi metodo randint")
            
            else:
                random.seed(1)
                with Check.input(['18']):
                    stdout = sys.stdout
                    sys.stdout = io.StringIO()
                    exec(koda)
                    output = sys.stdout.getvalue()
                    sys.stdout = stdout
                    output = output.strip()
                    if 'Čestitam! Odgovor je pravilen. Za odgovor si potreboval' not in output:
                        Check.error("Izpis ob pravilnem uporabnikovem odgovoru je napačen.")
                        
                with Check.input(['20']):
                    stdout = sys.stdout
                    sys.stdout = io.StringIO()
                    exec(koda)
                    output = sys.stdout.getvalue()
                    sys.stdout = stdout
                    output = output.strip()
                    if 'al narobe' not in output or 'Prav je 4' not in output or 'Za odgovor si potreboval' not in output:
                        Check.error("Izpis ob napačnem uporabnikovem odgovoru je napačen.")
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoxNzMxN30:1gIsjW:lYZ4rteT1tGnLOJQetT95TKauDY'
        try:
            import random
            odg = Check.current_part['solution']
            if "uniform" not in odg:
                if "random(" in odg:
                    Check.error("Res je, lahko uporabimo tudi metodo random() in malo računanja. " +
                                "Ampak obstaja tudi metoda, ki kar vrne ustrezno število. Poišči jo!")
                else:
                    Check.error("Hm, si našel pravo metodo za poljubno naključno število. Namig ... začne se na u.")
            
            vhod = [ ['2','2'], ['1','1'], ['-6','5']]
            izhod = ['4.824', '4.791', '1.226']
            random.seed(2)
            for i in range(len(vhod)):
                with Check.input(vhod[i]):
                    if not Check.output(Check.current_part['solution'], [
                        'Prvo število: ' + vhod[i][0],
                        'Drugo število: ' + vhod[i][1],
                        'Računam ...',
                        'Uf, je bilo težko. V '+ izhod[i] + ' sek so se moji čipi pošteno ogreli. Rezultat je: ' + str(int(vhod[i][0])*int(vhod[i][1])),
                        ]):
                        break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoxNzMxOH0:1gIsjW:s20WrB3R44D9fZNWyqi5nMHTx1o'
        try:
            vhod = [['4','7'], ['2','2'], ['1','1'], ['-6','5'], ['-3','-5']]
            
            for i in range(len(vhod)):
                vh = list(map(int, vhod[i]))
                if i == 3:
                    izh = [5.0, vh[0] * vh[1]]
                elif i == 4:
                    izh = [3.5, vh[0] * vh[1]]
                else:
                    izh = [min(vh[0]*vh[1]/10, 10), vh[0] * vh[1]]
                with Check.input(vhod[i]):
                    if not Check.output(Check.current_part['solution'], [
                        'Prvo število: ' + str(vh[0]),
                        'Drugo število: ' + str(vh[1]),
                        'Računam ...',
                        'Uf, je bilo težko. V ' + str(izh[0]) + ' sek so se moji čipi pošteno ogreli. Rezultat je: ' + str(izh[1]),
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
            print('Updating file... ', end="")
            backup_filename = backup(filename)
            with open(__file__, 'w', encoding='utf-8') as f:
                f.write(response['update'])
            print('Previous file has been renamed to {0}.'.format(backup_filename))
            print('If the file did not refresh in your editor, close and reopen it.')
    Check.summarize()

if __name__ == '__main__':
    _validate_current_file()
