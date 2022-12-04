import time

__all__ = ['info', 'warn', 'error']

def log(message, level, year, month, monthday, hour, minute, second, weekday, yearday):
    print(f'{monthday}-{month}-{year} {hour}:{minute}:{second} PICO {level}: {message}')

def info(message):
    log(message, 'INFO', *time.localtime())
  
def warn(message):
    log(message, 'WARN', *time.localtime())
 
def error(message):
    log(message, 'ERROR', *time.localtime())
 