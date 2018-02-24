/*
 * main.c
 *
 *  Created on: 18 Feb 2018
 *      Author: Mikolaj Jaworski
 */

//includes ---------------------------------------------------------------------------------------------------------------
#include "clock_config.h"  //MCUXPRESSO clock configuration tool----------------------------------------------------------
#include "MKE02Z4.h"

//Peripheral drivers for fsl API------------------------------------------------------------------------------------------
#include "fsl_adc.h"
#include "fsl_common.h"
#include "fsl_gpio.h"
#include "fsl_port.h"
#include "fsl_uart.h"

//variables---------------------------------------------------------------------------------------------------------------
volatile uint32_t msTicks = 0;

//functions---------------------------------------------------------------------------------------------------------------
void SysTick_Handler() {
    msTicks += 1;
}

//SysTick delay function--------------------------------------------------------------------------------------------------
void delay(uint32_t ms) {
    uint32_t returnTime = msTicks + ms;
    while (msTicks < returnTime) {}
}

//Initialization of GPIO port B, initialized as output--------------------------------------------------------------------
void gpio_Init(void)
{

	gpio_pin_config_t port_handler = { kGPIO_DigitalOutput, 1 };
	GPIO_PinInit(kGPIO_PORTB, 0U, &port_handler);


}
//Initialization of ADC in 12-bit resolution mode with continuous conversion and assigned to pin PTA0(channel0)-----------
void adc_Init(void)
{	//Enables hadc as handler for ADC-------------------------------------------------------------------------------------
	adc_config_t hadc;
	ADC_GetDefaultConfig(&hadc);
	hadc.ResolutionMode = kADC_Resolution12BitMode;
	ADC_Init(ADC, &hadc);

	//Enables channels and conversion types-------------------------------------------------------------------------------
	adc_channel_config_t chan_config;

	chan_config.channelNumber = 0U;
	chan_config.enableContinuousConversion = 1;
	chan_config.enableInterruptOnConversionCompleted = 1;

}

//Initialization of UART0 to port A1 and A3, with 9600 baud, with interrupt at RX-----------------------------------------
void uart_Init (void)
{
	//UART0 assigned to port A1 RX, and port A3 TX------------------------------------------------------------------------
	PORT_SetPinSelect(kPORT_UART0, kPORT_UART0_RXPTA2_TXPTA3);
	//Sets huart as handler for uart_config_t----------------------------------------------------------------------------
	 uart_config_t huart0;
	UART_GetDefaultConfig(&huart0);
	UART_SetBaudRate(UART0, 9600, 10000000U);
	//Interrupt at edge detection of RX----------------------------------------------------------------------------------
	UART_EnableInterrupts(UART0,kUART_RxActiveEdgeInterruptEnable);


}

//main loop---------------------------------------------------------------------------------------------------------------
int main(void)
{
	//Initialization function call----------------------------------------------------------------------------------------
	SysTick_Handler();
	gpio_Init();
	adc_Init();
	uart_Init();

	//Infinite loop-------------------------------------------------------------------------------------------------------
	while(1)
	{
		//BLinky led code-------------------------------------------------------------------------------------------------
		GPIO_PortToggle(kGPIO_PORTB, 0U);
		delay(200);

	}

}




