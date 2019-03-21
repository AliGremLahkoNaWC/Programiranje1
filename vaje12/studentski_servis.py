# =============================================================================
# Študentski servis
# =====================================================================@019428=
# 1. podnaloga
# Po koncu poletnega izpitnega obdobja si ugotovil, da imaš premalo denarja
# za potovanje, na katerega odhajaš čez slab mesec. Zato greš hitro pogledat
# na študentski servis, kako bi v tem času lahko zaslužil čimveč denarja.
# Denimo, da lahko delaš 22 dni.
# Našel si štiri ponudbe za delo in sicer
# * montaža, 6 dni, zaslužek: 300€
# * razvoz, 10 dni, zaslužek: 440€
# * anketiranje, 8 dni, zaslužek: 310€
# * pomoč v kuhinji, 15 dni, zaslužek: 900€
# Seveda želiš izbrati tista opravila, s katerimi boš v treh tednih zaslužil
# čimveč.
# Sestavi funkcijo `zasluzek(opravila, cas)`, ki bo, s pregledom vseh možnih
# kombinacij izbire opravil, vrnila največji možni zaslužek v danem času.
# Opravila so podana v tabeli `opravila`, ki jo sestavljajo pari
# `(trajanje, zasluzek)`.
# 
#     >>>zasluzek([(6, 300), (10, 440), (8, 310), (15, 900)], 22)
#     1200
# 
# Namig: verjetno si lahko pomagaš tudi z rešitvijo naloge 0/1 tabela.
# =============================================================================
def zasluzek(opravila, cas):
    novo=[]
    kombinacije=[]
    najbolje=[]
    denar=[]
    maximalno=0
    for x in opravila:
        caspoindeksih=[]
        if x[0]<cas:
            caspoindeksih.append(x[0])
            caspoindeksih.append(x[1])
            novo.append(caspoindeksih)
    for x in novo:
        for y in novo:
            if y !=x:
                cas1=x[0]+y[0]
                denar=x[1]+y[1]
                kombinacije.append([cas1,denar])
    use=[]
    for x in kombinacije:
        if x[0]<=cas and x not in use:
            use.append(x)
    if len(use)==0:
        for x in novo:
            if x[1]>maximalno:
                maximalno=x[1]
        return maximalno
    else:
        for x in use:
            if x[1]>maximalno:
                maximalno=x[1]
        return maximalno
    
# =====================================================================@019429=
# 2. podnaloga
# Poznavanje največjega možnega zaslužka nam ne koristi, če ne vemo pri
# kakšni izbiri opravil ga dosežemo. Sestavi funkcijo `katera(opravila, cas)`,
# ki vrne tabelo enake dolžine kot tabela `opravila` in vsebuje enice na
# indeksih, ki sovpadajo z izbranimi opravili, na ostalih indeksih pa ničle.
# Nalogo reši s pregledom vseh možnih kombinacij izbire opravil.
# 
#     >>>katera([(6, 300), (10, 440), (8, 310), (15, 900)], 22)
#     [1, 0, 0, 1]
# =============================================================================
def katera(opravila, cas):
    novo=[]
    kombinacije=[]
    najbolje=[]
    denar=[]
    maximalno=0
    kajdelamo=[]
    for x in opravila:
        caspoindeksih=[]
        if x[0]<cas:
            caspoindeksih.append(x[0])
            caspoindeksih.append(x[1])
            novo.append(caspoindeksih)
    for x in range(0,len(novo)):
        for y in range(0,len(novo)):
            if y !=x:
                cas1=novo[x][0]+novo[y][0]
                denar=novo[x][1]+novo[y][1]
                kombinacije.append([cas1,denar,x,y])
    use=[]
    stevec=0
    kajbo=[]
    for x in kombinacije:
        if x[0]<=cas and x not in use:
            use.append(x)
        stevec+=1
    if len(use)==0:
        for x in novo:
            if x[1]>maximalno:
                maximalno=x[1]
        for x in range(0,len(opravila)):
            if opravila[x][1]==maximalno:
                kajbo.append(1)
            else:
                kajbo.append(0)
        return kajbo
    else:
        for x in use:
            if x[1]>maximalno:
                maximalno=x[1]
                kajdelamo=[x[2],x[3]]
    for x in range(0,len(opravila)):
        if x==kajdelamo[0] or x==kajdelamo[1]:
            kajbo.append(1)
        else:
            kajbo.append(0)
    return kajbo
# =====================================================================@019430=
# 3. podnaloga
# Pregled vseh možnih kombinacij izbire opravil je zamuden postopek.
# Na predavanjih smo zato sestavili družino rekurzivnih funkcij,
# s katerimi lahko izračunamo največji možni zaslužek za poljubno število dni.
# I-ta funkcija upošteva prvih i opravil na voljo.
# 
# Funkcije (rečemo jim tudi Bellmanove enačbe) so oblike
# 
#   $$G_i(Č) = max( G_{i-1}(Č), zaslužek_i + G_{i-1}(Č - trajanje_i))$$
# 
# Sestavi funkcijo `zasluzek_bellman(opravila, cas)`, ki zgornjo nalogo reši
# z rekurzivno bellmanovo enačbo.
# 
#     >>>zasluzek_bellman([(6, 300), (10, 440), (8, 310), (15, 900)], 22)
#     1200
# =============================================================================

# =====================================================================@019431=
# 4. podnaloga
# Tudi za zgornji postopek bi bilo smiselno, da bi vedeli, katera opravila
# smo izbrali. 
# 
#     >>>katera_bellman([(6, 300), (10, 440), (8, 310), (15, 900)], 22)
#     [1, 0, 0, 1]
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
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoxOTQyOH0:1gmjcD:7EqwVMsv3czxswDwpG7ZqWhU0ec'
        try:
            tests = [('''zasluzek([(6, 300), (10, 440), (8, 310), (15, 900)], 11)''', 440),
                     ('''zasluzek([(6, 300), (10, 440), (8, 310), (15, 900)], 5)''', 0),
                     ('''zasluzek([(6, 300), (10, 440), (8, 310), (15, 900)], 7)''', 300),
                     ('''zasluzek([(6, 300), (10, 440), (8, 310), (15, 900)], 22)''', 1200),
                     ('''zasluzek([(6, 300), (10, 440), (8, 310), (15, 900)], 21)''', 1200),
                     ('''zasluzek([(6, 300), (10, 440), (8, 310), (15, 900)], 24)''', 1210)]
            
            for test in tests:
                if not Check.equal(*test):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoxOTQyOX0:1gmjcD:KsB8DktK8FRQvCc1ZqQjtPPzZAs'
        try:
            tests = [('''katera([(6, 300), (10, 440), (8, 310), (15, 900)], 11)''', [0, 1, 0, 0]),
                     ('''katera([(6, 300), (10, 440), (8, 310), (15, 900)], 5)''', [0, 0, 0, 0]),
                     ('''katera([(6, 300), (10, 440), (8, 310), (15, 900)], 7)''', [1, 0, 0, 0]),
                     ('''katera([(6, 300), (10, 440), (8, 310), (15, 900)], 22)''', [1, 0, 0, 1]),
                     ('''katera([(6, 300), (10, 440), (8, 310), (15, 900)], 21)''', [1, 0, 0, 1]),
                     ('''katera([(6, 300), (10, 440), (8, 310), (15, 900)], 24)''', [0, 0, 1, 1])]
            
            for test in tests:
                if not Check.equal(*test):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoxOTQzMH0:1gmjcD:HdgOoopGWQfaSDDgTQS1Zgn1Pd8'
        try:
            tests = [('''zasluzek_bellman([(6, 300), (10, 440), (8, 310), (15, 900)], 11)''', 440),
                     ('''zasluzek_bellman([(6, 300), (10, 440), (8, 310), (15, 900)], 5)''', 0),
                     ('''zasluzek_bellman([(6, 300), (10, 440), (8, 310), (15, 900)], 7)''', 300),
                     ('''zasluzek_bellman([(6, 300), (10, 440), (8, 310), (15, 900)], 22)''', 1200),
                     ('''zasluzek_bellman([(6, 300), (10, 440), (8, 310), (15, 900)], 24)''', 1210)]
            
            for test in tests:
                if not Check.equal(*test):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjozMzY3LCJwYXJ0IjoxOTQzMX0:1gmjcD:jFyhS4PkhL7z8IAEmfZmrmVQxCk'
        try:
            tests = [('''katera_bellman([(3, 300), (10, 440), (8, 310), (15, 900)], 5)''', [1, 0, 0, 0]),
                     ('''katera_bellman([(6, 300), (10, 440), (8, 310), (15, 900)], 11)''', [0, 1, 0, 0]),
                     ('''katera_bellman([(6, 300), (10, 440), (8, 310), (15, 900)], 5)''', [0, 0, 0, 0]),
                     ('''katera_bellman([(6, 300), (10, 440), (8, 310), (15, 900)], 7)''', [1, 0, 0, 0]),
                     ('''katera_bellman([(6, 300), (10, 440), (8, 310), (15, 900)], 22)''', [1, 0, 0, 1]),
                     ('''katera_bellman([(6, 300), (10, 440), (8, 310), (15, 900)], 24)''', [0, 0, 1, 1])]
            
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
