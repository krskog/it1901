package no.ntnu.it190121;

import java.util.Calendar;

public class Reservation {
	
	//Trenges dette i det hele tatt? Eller skal alt inn i koieklassen?
	
	private String address;
	private Calendar date; //Er dette den greieste måten å lagre datoen på?
	
	public Reservation(Calendar date, String address) {
		this.date = date;
		this.address = address;
	}

	public String getAddress() {
		return address;
	}

	public Calendar getDate() {
		return date;
	}
}
