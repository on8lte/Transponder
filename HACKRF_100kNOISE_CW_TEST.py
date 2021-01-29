#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Hackrf 100Knoise Cw Test
# Generated: Fri Jan 29 22:12:45 2021
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import osmosdr
import time


class HACKRF_100kNOISE_CW_TEST(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Hackrf 100Knoise Cw Test")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate_HACKRF = samp_rate_HACKRF = int(2e6)
        self.samp_rate = samp_rate = int(100e3)
        self.ditpersecond = ditpersecond = 8
        self.RF_freq = RF_freq = 433000000
        self.Freq_trim = Freq_trim = 40

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=samp_rate_HACKRF,
                decimation=samp_rate,
                taps=None,
                fractional_bw=None,
        )
        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + '' )
        #self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + 'hackrf=0' )
        self.osmosdr_sink_0.set_sample_rate(samp_rate_HACKRF)
        self.osmosdr_sink_0.set_center_freq(RF_freq, 0)
        self.osmosdr_sink_0.set_freq_corr(Freq_trim, 0)
        self.osmosdr_sink_0.set_gain(10, 0)
        self.osmosdr_sink_0.set_if_gain(20, 0)
        self.osmosdr_sink_0.set_bb_gain(20, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)

        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, int(50e3), int(5e3), firdes.WIN_HAMMING, 6.76))
        self.high_pass_filter_0 = filter.fir_filter_ccf(1, firdes.high_pass(
        	1, samp_rate, 3000, 300, firdes.WIN_HAMMING, 6.76))
        self.blocks_vector_source_x_0 = blocks.vector_source_c((1,1,1,0,1,1,1,01,1,1,0,0,0,0,1,1,1,0,0,0,1,0,0,0,0,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1,1,1,0), True, 1, [])
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_gr_complex*1, samp_rate/ditpersecond)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 2000, 0.1, 0)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 0.5, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.high_pass_filter_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_repeat_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_repeat_0, 0))
        self.connect((self.high_pass_filter_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.low_pass_filter_0, 0), (self.osmosdr_sink_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.low_pass_filter_0, 0))

    def get_samp_rate_HACKRF(self):
        return self.samp_rate_HACKRF

    def set_samp_rate_HACKRF(self, samp_rate_HACKRF):
        self.samp_rate_HACKRF = samp_rate_HACKRF
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate_HACKRF)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, int(50e3), int(5e3), firdes.WIN_HAMMING, 6.76))
        self.high_pass_filter_0.set_taps(firdes.high_pass(1, self.samp_rate, 3000, 300, firdes.WIN_HAMMING, 6.76))
        self.blocks_repeat_0.set_interpolation(self.samp_rate/self.ditpersecond)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_ditpersecond(self):
        return self.ditpersecond

    def set_ditpersecond(self, ditpersecond):
        self.ditpersecond = ditpersecond
        self.blocks_repeat_0.set_interpolation(self.samp_rate/self.ditpersecond)

    def get_RF_freq(self):
        return self.RF_freq

    def set_RF_freq(self, RF_freq):
        self.RF_freq = RF_freq
        self.osmosdr_sink_0.set_center_freq(self.RF_freq, 0)

    def get_Freq_trim(self):
        return self.Freq_trim

    def set_Freq_trim(self, Freq_trim):
        self.Freq_trim = Freq_trim
        self.osmosdr_sink_0.set_freq_corr(self.Freq_trim, 0)


def main(top_block_cls=HACKRF_100kNOISE_CW_TEST, options=None):

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
