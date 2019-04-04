# =============================================================================
# Golf
#
# Na vsakem zanimivem igrišču za golf so ovire: jezero, pesek, ...
# 
# `Jezero` je krog, podan kot trojica `(x,y,r)`.
# `Pesek` je pravokotnik, podan kot četverica`(x1,y1,x2,y2)`. Predpostaviš lahko, da 
# so to po vrsti koordinate levega spodnjega in desnega zgornjega oglišča.
# Vse koordinate računamo na tri decimalke (`round(x, 3)`)
# =====================================================================@019468=
# 1. podnaloga
# Na datoteki imamo zapisane podatke o posameznih udarcih v obliki polarnih koordinat (kot
# je podan v stopinjah).
# V vsaki vrstici sta zapisani celi števili `r` in `fi`, ločeni s presledkom.
# Napišite metodo `datotekaPolozajev(vhod, izhod)`, ki naj datoteko prebere in v tvori novo datoteko tako,
# da je v vsaki vrstici
# zapisan njen trenutni položaj (v obliki decimalnih števil, zaokroženih na 3 decimalna mesta)
# in ločenih s presledkom. V ta namen uporabite formatiranje s pomočjo "{0:.3f}".format(x)
# Začetni položaj naj bo v točki `(0,0)`.
# =============================================================================
import math
def datotekaPolozajev(vhod, izhod):
    '''funkcija vpisuje trenutne koordinate poleg vrstice vhodnih podatkov'''
    datoteka = open(izhod, 'w+')
    for vrstica in open(vhod, 'r'):
        vrstica = vrstica.split(' ')
        r = int(vrstica[0])
        fi = int(vrstica[1])
        x = r*math.cos(math.radians(fi))
        y = r*math.sin(math.radians(fi))
        print(x,y)
    datoteka.close()
    return datoteka
        
        
# =====================================================================@019469=
# 2. podnaloga
# Podan je seznam položajev žogic po posameznem udarcu in seznam, katerega vsak element
# je nabor, ki podaja jezero ali pesek. Napišite metodo `seIzogne(pot, ovire)`, ki pove, ali
# se pot v celoti izogne oviram. Pazi: jezero je podano z naborom treh, pesek pa z naborom štirih števil.
# 
# Najprej napišite metodi `jeVJezeru(zogica, jezero)` in `jeVPesku(zogica, pesek)`, ki
# povesta, ali je žogica v jezeru ali v pesku. Žogica je podana kot par `(x,y)`, torej "nima dimenzije".
# =============================================================================

# =====================================================================@019470=
# 3. podnaloga
# Napišite metodo `kjeJeZogica(datoteka, zacetek, ovire)`, ki
# vrne vektor od začenega do končnega položaja ali None,
# če žogica kdaj vmes pade v oviro.
# Posamezni udarci so v polarnih koordinatah zapisani na datoteko, začetek pa je
# podan kot par `(x,y)`.
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
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoxOTQ2OH0:1hC2GJ:LtvlFDGH8cplIbliU3jDpIF3OJM'
        try:
            def _makefile1(fname, ponovitev):
             with open(fname, "w") as f:
                 for i in range(ponovitev):
                     print("1 90", file=f)
                     print("2 -30", file=f)
                     print("2 210", file=f)
                     print("1 90", file=f)
            
            def _makefile2(fname, ponovitev):
             with open(fname, "w") as f:
                 for i in range(ponovitev):
                     print("0.000 1.000", file=f)
                     print("1.732 0.000", file=f)
                     print("0.000 -1.000", file=f)
                     print("0.000 0.000", file=f)
            
            def _istedatoteke(ena,dva):
             with open(ena) as f1, open(dva) as f2:
                 vrste1 = f1.read().strip()
                 vrste2 = f2.read().strip()
                 if vrste1 == vrste2:
                     return True
                 else:
                     print("Izhodna datoteka vsebuje naslednje vrstice: ")
                     print(vrste1)
                     print("Morala pa bi vsebovati naslednje vrstice: ")
                     print(vrste2)
             
            def _removefiles(*ime):
             import os
             for i in ime: os.remove(i)
            
            _makefile1("_3d.in",1)
            _makefile2("_3do.out",1)
            datotekaPolozajev("_3d.in","_3d.out")
            if not _istedatoteke("_3d.out", "_3do.out"):
                Check.error("Izhodna datoteka je napačna")
            _makefile1("_3d1.in",2)
            _makefile2("_3do1.out",2)
            datotekaPolozajev("_3d1.in","_3d1.out")
            if not _istedatoteke("_3d1.out", "_3do1.out"):
                Check.error("Izhodna datoteka je napačna")
            _removefiles("_3d.in", "_3do.out","_3d.out", "_3d1.in", "_3do1.out","_3d1.out")
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoxOTQ2OX0:1hC2GJ:bbi87bZZM4jogRsFYsE7Yv1Lu20'
        try:
            Check.equal('seIzogne([(0,0),(1,2),(3,4)],[(2,3,4),(1,1,2,2)])', False)
            Check.equal('seIzogne([(1,1),(1,2),(3,4)],[(2,3,14),(1,1,2,2)])', False)
            Check.equal('seIzogne([(0,0),(0,1)],[(2,3,1),(1,1,2,2)])', True)
            Check.equal('seIzogne([(0,0),(1,2),(3,4)],[(2,3,1),(2,2,3,3)])', True)
            Check.equal('seIzogne([(1,1),(1,2),(3,4)],[(1,1,1),(1,1,2,2)])', False)
            Check.equal('seIzogne([(1,1),(1,2),(3,4)],[(0,0,1),(1,1,2,2)])', False)
            Check.equal('seIzogne([(0,2),(1,2),(3,4)],[(0,0,1),(1,1,2,2)])', False)
            Check.equal('seIzogne([(0,2),(1,3),(3,4)],[(0,0,1),(1,1,2,2)])', True)
            Check.equal('seIzogne([(0,2),(1,3),(3,4),(0,2),(1,3),(3,4)],[(0,0,1),(1,1,2,2)])', True)
            Check.equal('seIzogne([(0,2)],[(0,0,1),(1,1,2,2)])', True)
            Check.equal('seIzogne([(0,2),(1,3),(3,4),(0,2),(1,3),(3,4)],[])', True)
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoxOTQ3MH0:1hC2GJ:t2nOkQ-B2xp8f4STVTqfRUExZgI'
        try:
            def _makefile1(fname,n):
             with open(fname, "w") as f:
                 poteze = ["1 90", "2 -30", "2 210", "1 90", "1 90", "2 -30", "2 210", "1 90", "1 90", "2 -30", "2 210", "1 90"]
                 for i in range(min(n, len(poteze))):
                    print(poteze[i], file=f)
                 
            _makefile1("_kje1.in", 4)
            _makefile1("_kje2.in", 1)
            _makefile1("_kje3.in", 12)
            _makefile1("_kje4.in", 11)
            _makefile1("_kje5.in", 10) 
            Check.equal('kjeJeZogica("_kje1.in",(0,0), [(2,3,4),(1,1,2,2)])', None)
            Check.equal('kjeJeZogica("_kje1.in",(0,0), [(2,3,1),(2,2,3,3)])', (0, 0))
            Check.equal('kjeJeZogica("_kje2.in",(0,0), [(2,3,1),(1,1,2,2)])', (0, 1))
            Check.equal('kjeJeZogica("_kje2.in",(0,0), [(0,0,2),(2,2,3,3)])', None)
            Check.equal('kjeJeZogica("_kje3.in",(0,0), [(2,3,4),(1,1,2,2)])', None)
            Check.equal('kjeJeZogica("_kje3.in",(0,0), [(0,0,0.5),(1,1,2,2)])', None)
            Check.equal('kjeJeZogica("_kje3.in",(0,0), [(0,0,0.5),(-1,-1,2,2)])', None)
            Check.equal('kjeJeZogica("_kje3.in",(0,0), [(2,3,1),(2,2,3,3)])', (0, 0))
            Check.equal('kjeJeZogica("_kje3.in",(0,0), [(2,3,1),(1,1,3,3)])', (0, 0))
            Check.equal('kjeJeZogica("_kje4.in",(0,0), [(2,3,1),(2,2,3,3)])', (0, -1))
            Check.equal('kjeJeZogica("_kje4.in",(0,0), [(2,3,1),(1,1,3,3)])', (0, -1))
            Check.equal('kjeJeZogica("_kje5.in",(0,0), [(2,3,1),(1,1,3,3)])', (1.732, 0.0))
            _removefiles("_kje1.in", "_kje2.in", "_kje3.in", "_kje4.in", "_kje5.in")
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
