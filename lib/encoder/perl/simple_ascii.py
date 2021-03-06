#!/usr/bin/env python
'''
OWASP ZSC
https://www.owasp.org/index.php/OWASP_ZSC_Tool_Project
https://github.com/zscproject/OWASP-ZSC
http://api.z3r0d4y.com/
https://groups.google.com/d/forum/owasp-zsc [ owasp-zsc[at]googlegroups[dot]com ]
'''
import random
import string


def encode(f):
    var_name = '$' + ''.join(
        random.choice(string.ascii_lowercase + string.ascii_uppercase)
        for i in range(50))
    ascii_data = ''.join([str(ord(i))+'*' for i in f])[:-1]
    data = var_name + ' = "' + ascii_data + '";\n'
    var_str = '$' + ''.join(
        random.choice(string.ascii_lowercase + string.ascii_uppercase)
        for i in range(50))
    var_data = '$' + ''.join(
        random.choice(string.ascii_lowercase + string.ascii_uppercase)
        for i in range(50))
    var_ascii = '@' + ''.join(
        random.choice(string.ascii_lowercase + string.ascii_uppercase)
        for i in range(50))
    var_value = '$' + ''.join(
        random.choice(string.ascii_lowercase + string.ascii_uppercase)
        for i in range(50))
    func_name = ''.join(
        random.choice(string.ascii_lowercase + string.ascii_uppercase)
        for i in range(50))
    func_argv = '$' + ''.join(
        random.choice(string.ascii_lowercase + string.ascii_uppercase)
        for i in range(50))

    f = '''
%s
sub %s {
    %s = shift;
    %s = '';
    %s = split /\*/, %s;
    foreach my %s (%s) {
       %s .= chr(%s);
    }
    return %s;
}
%s = %s;
eval %s(%s);
''' % (data, func_name, func_argv, var_str, var_ascii, func_argv, var_value,
       var_ascii, var_str, var_value, var_str, var_data, var_name, func_name, 
       var_data)
    return f


def start(content,cli):
    return str(str('=begin\n') + str(content.replace(
        '=begin', '#=begin').replace('=cut', '#=cut')) + str('\n=cut') + str(
            encode(content)) + str('\n'))
