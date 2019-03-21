# =============================================================================
# Veliki šef in njegovi podrejeni
#
# V nekem uspešnem podjetju ima skoraj vsak zaposleni svojega šefa. Seveda
# imajo tudi šefi svoje šefe in ti spet svoje šefe itn. Dobili smo podatke
# o hierarhiji v podjetju in ugotovili, da velja naslednje:
# 
# * Vsaka oseba ima kvečjemu enega šefa.
# * En šef ima lahko pod seboj več zaposlenih.
# * Vsem, ki so nad nami (naš šef, šef našega šefa itd.), pravimo _nadrejeni_.
# * Vsem, ki so pod nami (sami smo njihov šef, ali pa smo šef njihovega
#   šefa itd.), pravimo _podrejeni_.
# * Nihče ni sam svoj šef in nihče ni samemu sebi podrejen.
# 
# Napisali bomo nekaj funkcij, s katerimi bomo preučili razmere v podjetju.
# =====================================================================@019542=
# 1. podnaloga
# Podatke smo dobili v obliki tabele parov oblike `(uslužbenec, šef)`.
# Vsi uslužbenci so predstavljeni z nizi (ki so običajno njihova imena oz.
# priimki). Zgled:
# 
#     [('Mojca', 'Tilen'), ('Andrej', 'Tilen'), ('Tilen', 'Zoran')]
# 
# Komentar: Tilen ima pod seboj dva podrejena (Andreja in Mojco), njegovi
# šef pa je Zoran. Zoran nima šefa, vsi ostali pa so njegovi podrejeni.
# 
# Napišite funkcijo `slovar_sefov(tabela)`, ki bo iz zgoraj opisane
# tabele zgradila slovar šefov. Ključi v slovarju naj bodo uslužbenci,
# vrednosti pa njihovi šefi. Zgled:
# 
#     >>> slovar_sefov([('Mojca', 'Tilen'), ('Andrej', 'Tilen'), ('Tilen', 'Zoran')])
#     {'Andrej': 'Tilen', 'Mojca': 'Tilen', 'Tilen': 'Zoran'}
# =============================================================================
def slovar_sefov(tabela):
    '''funkcija vrne slovar kdo je komu sef'''
    slovar = dict()

    for relacija in tabela:
        slovar[relacija[0]] = relacija[1]
    return slovar
# =====================================================================@019543=
# 2. podnaloga
# Napišite funkcijo `neposredno_podrejeni(tabela)`, ki bo iz zgoraj opisane
# tabele sestavila slovar neposredno podrejenih. Vrednost pri vsakem
# ključu naj bo _množica_ tistih uslužbencev, ki imajo le-ta ključ za svojega
# šefa. Zgled:
# 
#     >>> neposredno_podrejeni([('Mojca', 'Tilen'), ('Andrej', 'Tilen'), ('Tilen', 'Zoran')])
#     {'Zoran': {'Tilen'}, 'Tilen': {'Andrej', 'Mojca'}}
# 
# Zoranu je torej neposredno podrejen le Tilen, Tilnu pa sta podrejena tako Andrej kot Mojca.
# =============================================================================
def neposredno_podrejeni(tabela):
    ''' funkcija sestavi slovar sefov hierarhicno'''
    slovar = slovar_sefov(tabela)
    nov_slovar = dict()

    for key, val in slovar.items():
        if val not in nov_slovar:
            nov_slovar[val] = {key}
        elif val in nov_slovar:
            nov_slovar[val].add(key)
    return nov_slovar
# =====================================================================@019544=
# 3. podnaloga
# Sestavite funkcijo `veriga_nadrejenih(usluzbenec, slovar)`, ki kot prvi
# argument dobi niz, ki predstavlja nekega uslužbenca, kot drugi argument
# pa dobi slovar šefov (v obliki kot ga vrne funkcija `slovar_sefov`).
# Funkcija naj sestavi tabelo, ki po vrsti vsebuje: šefa osebe `usluzbenec`,
# šefa od njegovega šefa itn. (dokler končno ne pridemo do osebe, ki nima šefa).
# Zgled:
# 
#     >>> veriga_nadrejenih('Mojca', {'Andrej': 'Tilen', 'Mojca': 'Tilen', 'Tilen': 'Zoran'})
#     ['Tilen', 'Zoran']
# 
# Mojci je nadrejen Tilen, kateremu je nadrejen Zoran, torej sta Mojčina šefa
# Tilen in Zoran.
# =============================================================================
def veriga_nadrejenih(usluzbenec,slovar):
    ''' funkcija vrne vse nadrejene usluzbenca'''
    tab = []

    for key, val in slovar.items():
        if key == usluzbenec:
            tab.append(val)
            usluzbenec = val
    return tab
# =====================================================================@019545=
# 4. podnaloga
# Sestavite funkcijo `mnozica_podrejenih(usluzbenec, slovar)`, ki kot prvi
# argument dobi ime uslužbenca, kot drugi argument pa slovar neposredno
# podrejenih (v obliki kot ga vrne funkcija `neposredno_podrejeni`). Funkcija
# naj sestavi in vrne _množico_ vseh tistih oseb, ki so (posredno ali
# neposredno) podrejeni osebi `usluzbenec`. Zgled:
# 
#     >>> mnozica_podrejenih('Zoran', {'Zoran': {'Tilen'}, 'Tilen': {'Andrej', 'Mojca'}, 'Mojca' : {'Urša'}})
#     {'Andrej', 'Mojca', 'Tilen', 'Urša'}
# 
# Zoranju je neposredno podrejen Tilen, torej sta mu podrejena tudi Tilnova
# podrejena Andrej in Mojca, ter Urša, ker je ta podrejena Mojci.
# =============================================================================
def mnozica_podrejenih(usluzbenec,slovar):
    ''' funkcija vrne mnozico ljudi ki so podrejeni usluzbencu'''
    podrejeni = set()
    for key, val in slovar.items():
        if key == usluzbenec:
           for oseba in val:
               podrejeni.add(oseba)
        elif key in podrejeni:
            for oseba in val:
                podrejeni.add(oseba)
    return podrejeni
    

# =====================================================================@019546=
# 5. podnaloga
# Tistemu uslužbencu, za katerega velja:
# 
# * da nima nadrejenih;
# * je zadnji v verigi nadrejenih vseh ostalih uslužbencev (razen seveda
#   samega sebe);
# 
# pravimo _big boss_. Sestavite funkcijo `big_boss(slovar)`, ki kot argument
# dobi slovar nadrejenih in vrne ime osebe, ki je big boss v podjetju oz.
# vrednost `None`, če to podjetje nima big boss-a. Zgled:
# 
#     >>> big_boss({'Andrej': 'Tilen', 'Mojca': 'Tilen', 'Tilen': 'Zoran'})
#     'Zoran'
# =============================================================================
def big_boss(slovar):
    ''' funkcija poizve kdo je glavni'''
    veliki_sef = None
    tab = []

    for key, val in slovar.items():
        veliki_sef = val
    return veliki_sef




































































































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
        Check.current_part['token'] = 'eyJwYXJ0IjoxOTU0MiwidXNlciI6MzM2N30:1h6s8N:5Grza5SIJIULeg9p_jGiAYiEw_o'
        try:
            # tests = [
            #         ("slovar_sefov([('Mojca', 'Tilen'), ('Andrej', 'Tilen'), ('Tilen', 'Zoran')])",
            #             {'Andrej': 'Tilen', 'Mojca': 'Tilen', 'Tilen': 'Zoran'}),
            #         ("slovar_sefov([('Mojca', 'Tilen'), ('Tilen', 'Tilen'), ('Tilen', 'Zoran')])",
            #             {'Mojca': 'Tilen', 'Tilen': 'Zoran'}),
            #         ("slovar_sefov([('Mojca', ''), ('', 'Tilen')])",
            #             {'': 'Tilen', 'Mojca': ''})
            #         ]
            
            # for test in tests:
            #     if not Check.equal(*test):
            #         break
            
            tests_secret = [
                    slovar_sefov([('Mojca', 'Tilen'), ('Andrej', 'Tilen'), ('Tilen', 'Zoran')]),
                    slovar_sefov([('Mojca', 'Tilen'), ('Tilen', 'Tilen'), ('Tilen', 'Zoran')]),
                    slovar_sefov([('Mojca', ''), ('', 'Tilen')])
                    ]
            
            for test in tests_secret:
                if not Check.secret(test):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoxOTU0MywidXNlciI6MzM2N30:1h6s8N:0WywMAZ77xoCE6bWezwmNtTk5ds'
        try:
            # tests = [
            #         ("neposredno_podrejeni([('Mojca', 'Tilen'), ('Andrej', 'Tilen'), ('Tilen', 'Zoran')])",
            #             {'Zoran': {'Tilen'}, 'Tilen': {'Andrej', 'Mojca'}}),
            #         ("neposredno_podrejeni([('Mojca', 'Tilen'), ('Tilen', 'Tilen'), ('Tilen', 'Zoran')])",
            #             {'Zoran': set(['Tilen']), 'Tilen': set(['Mojca', 'Tilen'])}),
            #         ("neposredno_podrejeni([('Mojca', ''), ('', 'Tilen')])",
            #             {'': set(['Mojca']), 'Tilen': set([''])})
            #         ]
            # 
            # for test in tests:
            #     if not Check.equal(*test):
            #         break
            
            tests_secret = [
                    neposredno_podrejeni([('Mojca', 'Tilen'), ('Andrej', 'Tilen'), ('Tilen', 'Zoran')]),
                    neposredno_podrejeni([('Mojca', 'Tilen'), ('Tilen', 'Tilen'), ('Tilen', 'Zoran')]),
                    neposredno_podrejeni([('Mojca', ''), ('', 'Tilen')]),
                    ]
            
            for test in tests_secret:
                if not Check.secret(test):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoxOTU0NCwidXNlciI6MzM2N30:1h6s8N:afwXCFcFeyIsDTASf2mBes90WEA'
        try:
            # tests = [
            #         ("veriga_nadrejenih('Mojca', {'Andrej': 'Tilen', 'Mojca': 'Tilen', 'Tilen': 'Zoran'})", ['Tilen', 'Zoran']),
            #         ("veriga_nadrejenih('Mojca', {'Andrej': 'Tilen', 'Mojca': 'Tilen', '': 'Zoran'})",['Tilen']),
            #         ("veriga_nadrejenih('Mojca', {'Andrej': 'Tilen', '': 'Tilen', 'Tilen': 'Zoran'})",[]),
            #         ("veriga_nadrejenih('Peter', {'Zoran' : 'Peter', 'Juš' : 'Peter', 'Sonja' : 'Peter', 'Andrej': 'Tilen', 'Peter' : 'Matija', 'Mojca': 'Tilen', 'Tilen': 'Zoran', 'Jaka' : 'Jan', 'Jan' : 'Zoran'})", ['Matija']),
            #         ("veriga_nadrejenih('Mojca', {'Zoran' : 'Peter', 'Juš' : 'Peter', 'Sonja' : 'Peter', 'Andrej': 'Tilen', 'Peter' : 'Matija', 'Mojca': 'Tilen', 'Tilen': 'Zoran', 'Jaka' : 'Jan', 'Jan' : 'Zoran'})", ['Tilen', 'Zoran', 'Peter','Matija']),
            #         ("veriga_nadrejenih('Sonja', {'Zoran' : 'Peter', 'Juš' : 'Peter', 'Sonja' : 'Peter', 'Andrej': 'Tilen', 'Peter' : 'Matija', 'Mojca': 'Tilen', 'Tilen': 'Zoran', 'Jaka' : 'Jan', 'Jan' : 'Zoran'})", ['Peter', 'Matija']),
            #         ("veriga_nadrejenih('Andrej', {'Zoran' : 'Peter', 'Juš' : 'Peter', 'Sonja' : 'Peter', 'Andrej': 'Tilen', 'Peter' : 'Matija', 'Mojca': 'Tilen', 'Tilen': 'Zoran', 'Jaka' : 'Jan', 'Jan' : 'Zoran'})", ['Tilen', 'Zoran', 'Peter','Matija'])
            #         ]
            # 
            # for test in tests:
            #     if not Check.equal(*test):
            #         break
            
            tests_secret = [
                    veriga_nadrejenih('Mojca', {'Andrej': 'Tilen', 'Mojca': 'Tilen', 'Tilen': 'Zoran'}),
                    veriga_nadrejenih('Mojca', {'Andrej': 'Tilen', 'Mojca': 'Tilen', '': 'Zoran'}),
                    veriga_nadrejenih('Mojca', {'Andrej': 'Tilen', '': 'Tilen', 'Tilen': 'Zoran'}),
                    veriga_nadrejenih('Peter', {'Zoran' : 'Peter', 'Juš' : 'Peter', 'Sonja' : 'Peter', 'Andrej': 'Tilen', 'Peter' : 'Matija', 'Mojca': 'Tilen', 'Tilen': 'Zoran', 'Jaka' : 'Jan', 'Jan' : 'Zoran'}),
                    veriga_nadrejenih('Mojca', {'Zoran' : 'Peter', 'Juš' : 'Peter', 'Sonja' : 'Peter', 'Andrej': 'Tilen', 'Peter' : 'Matija', 'Mojca': 'Tilen', 'Tilen': 'Zoran', 'Jaka' : 'Jan', 'Jan' : 'Zoran'}),
                    veriga_nadrejenih('Sonja', {'Zoran' : 'Peter', 'Juš' : 'Peter', 'Sonja' : 'Peter', 'Andrej': 'Tilen', 'Peter' : 'Matija', 'Mojca': 'Tilen', 'Tilen': 'Zoran', 'Jaka' : 'Jan', 'Jan' : 'Zoran'}),
                    veriga_nadrejenih('Andrej', {'Zoran' : 'Peter', 'Juš' : 'Peter', 'Sonja' : 'Peter', 'Andrej': 'Tilen', 'Peter' : 'Matija', 'Mojca': 'Tilen', 'Tilen': 'Zoran', 'Jaka' : 'Jan', 'Jan' : 'Zoran'}),
                    ]
            
            for test in tests_secret:
                if not Check.secret(test):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoxOTU0NSwidXNlciI6MzM2N30:1h6s8N:wV-gkEDm_YN-u6mVK6z-Mkxu5r8'
        try:
            # tests = [
            #         ("mnozica_podrejenih('Zoran', {'Zoran': {'Tilen'}, 'Tilen': {'Andrej', 'Mojca'}})", {'Andrej', 'Mojca', 'Tilen'}),
            #         ("mnozica_podrejenih('Zoran', {'': {'Tilen'}, 'Tilen': {'Andrej', 'Mojca'}})",set([])),
            #         ("mnozica_podrejenih('Tilen', {'Tilen': {'Andrej', 'Mojca', 'A'}})",set(['Andrej', 'Mojca', 'A'])),
            #         ("mnozica_podrejenih('T', {'T': {'A', 'M', 'B'}, 'A' : {'Q', 'W'}, 'B' : {'O'}})",set(['A', 'M', 'B','Q', 'W', 'O'])),
            #         ("mnozica_podrejenih('Zoran', {'Zoran': {'Tilen'}, 'Zoran': {'Andrej', 'Mojca'}})",set(['Andrej', 'Mojca'])),
            #         ("mnozica_podrejenih('Zoran', {'Zoran': {'Tilen'}, 'Tilen': {'Andrej', 'Mojca'}, 'Mojca' : {'Urša'}})", {'Andrej', 'Mojca', 'Tilen', 'Urša'}),
            #         ("mnozica_podrejenih('Zoran', {'Zoran': {'Tilen'}, 'Tilen': {'Andrej', 'Mojca', 'Tim'}, 'Tim' : {'Jaka'},  'Mojca' : {'Urša'}})", {'Andrej', 'Mojca', 'Tilen', 'Urša', 'Tim', 'Jaka'}),
            #         ("mnozica_podrejenih('Mojca', {'Zoran': {'Tilen'}, 'Tilen': {'Andrej', 'Mojca', 'Tim'}, 'Tim' : {'Jaka'},  'Mojca' : {'Urša'}})", {'Urša'}),
            #         ("mnozica_podrejenih('A', {'T': {'A', 'M', 'B'}, 'A' : {'Q', 'W'}, 'B' : {'O'}})",set(['Q', 'W'])),
            #         ("mnozica_podrejenih('B', {'T': {'A', 'M', 'B'}, 'A' : {'Q', 'W'}, 'B' : {'O'}})",set(['O'])),
            #         ("mnozica_podrejenih('A', {'T': {'A', 'M', 'B'}, 'A' : {'Q', 'Z'}, 'Z' : {'O'}, 'O' : {'J'}})",set(['Q','Z','O','J']))
            #         ]
            # 
            # for test in tests:
            #     if not Check.equal(*test):
            #         break
            
            tests_secret = [
                    mnozica_podrejenih('Zoran', {'Zoran': {'Tilen'}, 'Tilen': {'Andrej', 'Mojca'}}),
                    mnozica_podrejenih('Zoran', {'': {'Tilen'}, 'Tilen': {'Andrej', 'Mojca'}}),
                    mnozica_podrejenih('Tilen', {'Tilen': {'Andrej', 'Mojca', 'A'}}),
                    mnozica_podrejenih('T', {'T': {'A', 'M', 'B'}, 'A' : {'Q', 'W'}, 'B' : {'O'}}),
                    mnozica_podrejenih('Zoran', {'Zoran': {'Tilen'}, 'Zoran': {'Andrej', 'Mojca'}}),
                    mnozica_podrejenih('Zoran', {'Zoran': {'Tilen'}, 'Tilen': {'Andrej', 'Mojca'}, 'Mojca' : {'Urša'}}),
                    mnozica_podrejenih('Zoran', {'Zoran': {'Tilen'}, 'Tilen': {'Andrej', 'Mojca', 'Tim'}, 'Tim' : {'Jaka'},  'Mojca' : {'Urša'}}), 
                    mnozica_podrejenih('Mojca', {'Zoran': {'Tilen'}, 'Tilen': {'Andrej', 'Mojca', 'Tim'}, 'Tim' : {'Jaka'},  'Mojca' : {'Urša'}}),
                    mnozica_podrejenih('A', {'T': {'A', 'M', 'B'}, 'A' : {'Q', 'W'}, 'B' : {'O'}}),
                    mnozica_podrejenih('B', {'T': {'A', 'M', 'B'}, 'A' : {'Q', 'W'}, 'B' : {'O'}}),
                    mnozica_podrejenih('A', {'T': {'A', 'M', 'B'}, 'A' : {'Q', 'Z'}, 'Z' : {'O'}, 'O' : {'J'}}),
                    ]
            
            for test in tests_secret:
                if not Check.secret(test):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0IjoxOTU0NiwidXNlciI6MzM2N30:1h6s8N:ykf9R-NABQO2-h3-BritlkoZNSc'
        try:
            # tests = [
            #         ("big_boss({'Andrej': 'Tilen', 'Mojca': 'Tilen', 'Tilen': 'Zoran'})", 'Zoran'),
            #         ("big_boss({'Andrej': 'Tilen', 'Mojca': 'Jan', 'Tilen': 'Zoran'})", None),
            #         ("big_boss({'Andrej': 'Tilen', 'Mojca': 'Tilen', 'Tilen': 'Zoran', 'Jaka' : 'Jan', 'Jan' : 'Zoran'})", 'Zoran'),
            #         ("big_boss({'Zoran' : 'Peter', 'Andrej': 'Tilen', 'Mojca': 'Tilen', 'Tilen': 'Zoran', 'Jaka' : 'Jan', 'Jan' : 'Zoran'})", 'Peter'),
            #         ("big_boss({'Zoran' : 'Peter', 'Juš' : 'Peter', 'Sonja' : 'Peter', 'Andrej': 'Tilen', 'Mojca': 'Tilen', 'Tilen': 'Zoran', 'Jaka' : 'Jan', 'Jan' : 'Zoran'})", 'Peter'),
            #         ("big_boss({'Pavel' : 'Peter', 'Andrej': 'Tilen', 'Mojca': 'Tilen', 'Tilen': 'Zoran', 'Jaka' : 'Jan', 'Jan' : 'Zoran'})", None),
            #         ("big_boss({})", None),
            #         ("big_boss({'Zoran' : 'Peter', 'Juš' : 'Peter', 'Sonja' : 'Peter', 'Andrej': 'Tilen', 'Peter' : 'Matija', 'Mojca': 'Tilen', 'Tilen': 'Zoran', 'Jaka' : 'Jan', 'Jan' : 'Zoran'})", 'Matija'),
            #         ("big_boss({'Matej' : 'Mojca', 'Zoran' : 'Peter', 'Juš' : 'Peter', 'Sonja' : 'Peter', 'Andrej': 'Tilen', 'Peter' : 'Matija', 'Mojca': 'Tilen', 'Tilen': 'Zoran', 'Jaka' : 'Jan', 'Jan' : 'Zoran'})", 'Matija')
            #         ]
            # 
            # for test in tests:
            #     if not Check.equal(*test):
            #         break
            
            tests_secret = [
                    big_boss({'Andrej': 'Tilen', 'Mojca': 'Tilen', 'Tilen': 'Zoran'}),
                    big_boss({'Andrej': 'Tilen', 'Mojca': 'Jan', 'Tilen': 'Zoran'}),
                    big_boss({'Andrej': 'Tilen', 'Mojca': 'Tilen', 'Tilen': 'Zoran', 'Jaka' : 'Jan', 'Jan' : 'Zoran'}), 
                    big_boss({'Zoran' : 'Peter', 'Andrej': 'Tilen', 'Mojca': 'Tilen', 'Tilen': 'Zoran', 'Jaka' : 'Jan', 'Jan' : 'Zoran'}), 
                    big_boss({'Zoran' : 'Peter', 'Juš' : 'Peter', 'Sonja' : 'Peter', 'Andrej': 'Tilen', 'Mojca': 'Tilen', 'Tilen': 'Zoran', 'Jaka' : 'Jan', 'Jan' : 'Zoran'}),
                    big_boss({'Pavel' : 'Peter', 'Andrej': 'Tilen', 'Mojca': 'Tilen', 'Tilen': 'Zoran', 'Jaka' : 'Jan', 'Jan' : 'Zoran'}),
                    big_boss({}),
                    big_boss({'Zoran' : 'Peter', 'Juš' : 'Peter', 'Sonja' : 'Peter', 'Andrej': 'Tilen', 'Peter' : 'Matija', 'Mojca': 'Tilen', 'Tilen': 'Zoran', 'Jaka' : 'Jan', 'Jan' : 'Zoran'}),
                    big_boss({'Matej' : 'Mojca', 'Zoran' : 'Peter', 'Juš' : 'Peter', 'Sonja' : 'Peter', 'Andrej': 'Tilen', 'Peter' : 'Matija', 'Mojca': 'Tilen', 'Tilen': 'Zoran', 'Jaka' : 'Jan', 'Jan' : 'Zoran'}),
                    ]
            
            for test in tests_secret:
                if not Check.secret(test):
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
