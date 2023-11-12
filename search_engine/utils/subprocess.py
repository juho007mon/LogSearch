
import os
import logging
import subprocess

def run_cmd(cmd, cwd=None):
  '''Run a command, logging the output to the logging module, and return the output and status code'''
  if cwd is None:
    restore_dir = None
    cwd = os.getcwd()
  else:
    restore_dir = os.getcwd()
    os.chdir(cwd)
  os.environ['PWD'] = cwd

  output = ''

  logging.debug('CWD: %s', cwd)
  logging.debug('CMD: %s', ' '.join(cmd))

  # Set session ID on process, which will be inherited by its children
  proc = subprocess.Popen(
      cmd,
      stdin=subprocess.PIPE,
      stdout=subprocess.PIPE,
      stderr=subprocess.STDOUT,
      universal_newlines=True,
      preexec_fn=os.setsid)
  try:
    for line in proc.stdout:
      output += line
      logging.debug(line.rstrip())
    proc.wait()
  except KeyboardInterrupt:
    logging.error('Ctrl-c pressed - terminating process: %s', ' '.join(cmd))
    os.killpg(proc.pid, signal.SIGTERM)
    if restore_dir:
      os.chdir(restore_dir)
    raise

  if restore_dir:
    os.chdir(restore_dir)

  return {'return_code': proc.returncode, 'output': output}