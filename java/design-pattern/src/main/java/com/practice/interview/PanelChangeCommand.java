package com.practice.interview;

//	http://iilii.egloos.com/5378691
public class PanelChangeCommand implements ReversibleCommand	{
	private final Panel	panel;
	private final String	newColor;
	private final String	oldColor;
	public PanelChangeCommand(Panel panel, String newColor)	{
		this.panel	=	panel;
		this.oldColor	=	panel.getColor();
		this.newColor	=	newColor;
	}
	@Override
	public void redo()	{
		panel.setColor(newColor);
	}
	@Override
	public void undo()	{
		panel.setColor(oldColor);
	}
}

