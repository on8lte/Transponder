#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Linear Transponder
# Author: Anton JAnovsky
# Description: Satellite Linear Transponder
# Generated: Fri Jan 29 23:14:34 2021
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import osmosdr
import time


class Lin_transponder(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Linear Transponder")

        ##################################################
        # Variables
        ##################################################
        self.tx_freq = tx_freq = 438.1e6
        self.samp_rate = samp_rate = 2e6
        self.rx_freq = rx_freq = 145.3e6
        self.rf_gain = rf_gain = 50

        ##################################################
        # Blocks
        ##################################################
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(rx_freq, 0)
        self.rtlsdr_source_0.set_freq_corr(0, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(2, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(2, 0)
        self.rtlsdr_source_0.set_gain_mode(True, 0)
        self.rtlsdr_source_0.set_gain(50, 0)
        self.rtlsdr_source_0.set_if_gain(50, 0)
        self.rtlsdr_source_0.set_bb_gain(50, 0)
        self.rtlsdr_source_0.set_antenna('', 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)

        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + '' )
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(tx_freq, 0)
        self.osmosdr_sink_0.set_freq_corr(40, 0)
        self.osmosdr_sink_0.set_gain(10, 0)
        self.osmosdr_sink_0.set_if_gain(20, 0)
        self.osmosdr_sink_0.set_bb_gain(20, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)

        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, 100000, 50000, firdes.WIN_HAMMING, 6.76))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((2, ))



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.osmosdr_sink_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.low_pass_filter_0, 0))

    def get_tx_freq(self):
        return self.tx_freq

    def set_tx_freq(self, tx_freq):
        self.tx_freq = tx_freq
        self.osmosdr_sink_0.set_center_freq(self.tx_freq, 0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 100000, 50000, firdes.WIN_HAMMING, 6.76))

    def get_rx_freq(self):
        return self.rx_freq

    def set_rx_freq(self, rx_freq):
        self.rx_freq = rx_freq
        self.rtlsdr_source_0.set_center_freq(self.rx_freq, 0)

    def get_rf_gain(self):
        return self.rf_gain

    def set_rf_gain(self, rf_gain):
        self.rf_gain = rf_gain


def main(top_block_cls=Lin_transponder, options=None):

    tb = top_block_cls()
    tb.start()
    try:
        input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
