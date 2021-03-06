from __future__ import print_function

class Module(object):
    def __init__(self, boot):
        self._boot = boot

    def process(self, modules):
        print('===============================================')
        print('Pira     : status - voltage   : ' + str(self._boot.get_voltage()) + ' V')
        print('Pira     : status - rtc time  : {}'.format(self._boot.get_time()))
        print('Pira     : status - on timer s: {} s'.format(self._boot.get_pira_on_timer_set()))
        print('Pira     : status - on timer  : {} s'.format(self._boot.get_pira_on_timer()))
        print('Charging : {}'.format(self._boot.is_charging))
        print('Debug    : {}'.format(self._boot.is_debug_enabled))
        #print('Temp.    : {}'.format(self._boot.rtc.temperature))

        # Report distance measured by ultrasonic module if enabled.
        if 'pira.modules.ultrasonic' in modules:
            print('Distance : {}'.format(modules['pira.modules.ultrasonic'].distance))

    def shutdown(self, modules):
        """Shutdown module."""
        pass
