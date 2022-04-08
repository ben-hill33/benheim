# Read: 14b - CSS Transforms, Transitions, and Animations

## Assorted Articles

### [Transforms](https://learn.shayhowe.com/advanced-html-css/css-transforms/)

With CSS3 came new ways to position and alter elements. The **transform** property comes in two different settings, **two-dimensional** and **three-dimensional**. Each come with their own individual properties and values. 
**2D Transforms**
- Work on an x and y axis
- Accepts a handful of different values such as **rotate**, which provides the ability to rotate an element from 0-360 degrees. Positive value will rotate an element clockwise, negative rotates counterclockwise. The default point is center.
- Using **scale** values allows you to change the appeared size of an element. Default scale is 1. Anything below .99 and .01 makes element appear smaller, or above 1.01 makes element appear larger. 
- The **translate** value works a bit like that of relative positioning, pushing and pulling an element in different directions without interrupting the normal flow of the document. 
- **Skew** is used to distort elements on the x,y or both axes. skewX distorts an element on horizontal axis while skewY distorts elements on vertical. Distorting on both axes, declare x first, followed by comma, then y.
- You can combine these transform properties above. 
**3D Transorms**
- The biggest difference here between 2D is you can elements on the z axis, giving you control of depth in addition to length and and width. 

### [Transitions & Animations](https://learn.shayhowe.com/advanced-html-css/transitions-animations/)

With CSS3 transitions you have the potential to alter the appearance and behavior of an element whenever a state change occurs, such as when it is hovered over, focused on, active, or targeted. 
Animations allow the appearance of behavior of an element to be altered in multiple keyframes. 
**Transitions provide a change from one state to another, while animations can set multiple points of transtion upon different keyframes.**

**Transional properties**
- It is important to note, not all properties may be transitioned, only properties that have an identifiable halfway point. The display property, for example, may not be transitioned as it does not have any midpoint. 
- The **transition-duration** property can be set using general timing values including seconds and miliseconds. You can set multiple durations
- The **transition-timing-function** property is used to set the speed in which a transition will... transition. 

**Animations**
When more control is needed for transitions you can set animations for the transitions to have multiple states. 

#### Links:
- [8 Simple CSS Transitions to Wow your Users](https://www.webdesignerdepot.com/2014/05/8-simple-css3-transitions-that-will-wow-your-users/)
- [6 Buttons Animated](https://codepen.io/retyui/pen/ByoaXV)
- [CSS Animations: Keyframes](https://codepen.io/akshaychauhan/pen/oAfae)
- [404](https://codepen.io/kieranfivestars/pen/MYdQxX)
- [Pure CSS Bounce Animation](https://codepen.io/dp_lewis/pen/gCfBv)

  