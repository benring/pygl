from OpenGL.GL import *

colors = {
	'aliceblue' : (0.9411764705882353, 0.9725490196078431, 1.0),
	'antiquewhite' : (0.9803921568627451, 0.9215686274509803, 0.8431372549019608),
	'aqua' : (0.0, 1.0, 1.0),
	'aquamarine' : (0.4980392156862745, 1.0, 0.8313725490196079),
	'azure' : (0.9411764705882353, 1.0, 1.0),
	'beige' : (0.9607843137254902, 0.9607843137254902, 0.8627450980392157),
	'bisque' : (1.0, 0.8941176470588236, 0.7686274509803922),
	'black' : (0.0, 0.0, 0.0),
	'blanchedalmond' : (1.0, 0.9215686274509803, 0.803921568627451),
	'blue' : (0.0, 0.0, 1.0),
	'blueviolet' : (0.5411764705882353, 0.16862745098039217, 0.8862745098039215),
	'brown' : (0.6470588235294118, 0.16470588235294117, 0.16470588235294117),
	'burlywood' : (0.8705882352941177, 0.7215686274509804, 0.5294117647058824),
	'cadetblue' : (0.37254901960784315, 0.6196078431372549, 0.6274509803921569),
	'chartreuse' : (0.4980392156862745, 1.0, 0.0),
	'chocolate' : (0.8235294117647058, 0.4117647058823529, 0.11764705882352941),
	'coral' : (1.0, 0.4980392156862745, 0.3137254901960784),
	'cornflowerblue' : (0.39215686274509803, 0.5843137254901961, 0.9294117647058824),
	'cornsilk' : (1.0, 0.9725490196078431, 0.8627450980392157),
	'crimson' : (0.8627450980392157, 0.0784313725490196, 0.23529411764705882),
	'cyan' : (0.0, 1.0, 1.0),
	'darkblue' : (0.0, 0.0, 0.5450980392156862),
	'darkcyan' : (0.0, 0.5450980392156862, 0.5450980392156862),
	'darkgoldenrod' : (0.7215686274509804, 0.5254901960784314, 0.043137254901960784),
	'darkgray' : (0.6627450980392157, 0.6627450980392157, 0.6627450980392157),
	'darkgreen' : (0.0, 0.39215686274509803, 0.0),
	'darkgrey' : (0.6627450980392157, 0.6627450980392157, 0.6627450980392157),
	'darkkhaki' : (0.7411764705882353, 0.7176470588235294, 0.4196078431372549),
	'darkmagenta' : (0.5450980392156862, 0.0, 0.5450980392156862),
	'darkolivegreen' : (0.3333333333333333, 0.4196078431372549, 0.1843137254901961),
	'darkorange' : (1.0, 0.5490196078431373, 0.0),
	'darkorchid' : (0.6, 0.19607843137254902, 0.8),
	'darkred' : (0.5450980392156862, 0.0, 0.0),
	'darksalmon' : (0.9137254901960784, 0.5882352941176471, 0.47843137254901963),
	'darkseagreen' : (0.5607843137254902, 0.7372549019607844, 0.5607843137254902),
	'darkslateblue' : (0.2823529411764706, 0.23921568627450981, 0.5450980392156862),
	'darkslategray' : (0.1843137254901961, 0.30980392156862746, 0.30980392156862746),
	'darkturquoise' : (0.0, 0.807843137254902, 0.8196078431372549),
	'darkviolet' : (0.5803921568627451, 0.0, 0.8274509803921568),
	'deeppink' : (1.0, 0.0784313725490196, 0.5764705882352941),
	'deepskyblue' : (0.0, 0.7490196078431373, 1.0),
	'dimgray' : (0.4117647058823529, 0.4117647058823529, 0.4117647058823529),
	'dodgerblue' : (0.11764705882352941, 0.5647058823529412, 1.0),
	'firebrick' : (0.6980392156862745, 0.13333333333333333, 0.13333333333333333),
	'floralwhite' : (1.0, 0.9803921568627451, 0.9411764705882353),
	'forestgreen' : (0.13333333333333333, 0.5450980392156862, 0.13333333333333333),
	'gainsboro' : (0.8627450980392157, 0.8627450980392157, 0.8627450980392157),
	'ghostwhite' : (0.9725490196078431, 0.9725490196078431, 1.0),
	'gold' : (1.0, 0.8431372549019608, 0.0),
	'goldenrod' : (0.8549019607843137, 0.6470588235294118, 0.12549019607843137),
	'gray' : (0.5019607843137255, 0.5019607843137255, 0.5019607843137255),
	'green' : (0.0, 0.5019607843137255, 0.0),
	'greenyellow' : (0.6784313725490196, 1.0, 0.1843137254901961),
	'grey' : (0.5019607843137255, 0.5019607843137255, 0.5019607843137255),
	'honeydew' : (0.9411764705882353, 1.0, 0.9411764705882353),
	'hotpink' : (1.0, 0.4117647058823529, 0.7058823529411765),
	'indianred' : (0.803921568627451, 0.3607843137254902, 0.3607843137254902),
	'indigo' : (0.29411764705882354, 0.0, 0.5098039215686274),
	'ivory' : (1.0, 1.0, 0.9411764705882353),
	'khaki' : (0.9411764705882353, 0.9019607843137255, 0.5490196078431373),
	'lavender' : (0.9019607843137255, 0.9019607843137255, 0.9803921568627451),
	'lavenderblush' : (1.0, 0.9411764705882353, 0.9607843137254902),
	'lawngreen' : (0.48627450980392156, 0.9882352941176471, 0.0),
	'lemonchiffon' : (1.0, 0.9803921568627451, 0.803921568627451),
	'lightblue' : (0.6784313725490196, 0.8470588235294118, 0.9019607843137255),
	'lightcoral' : (0.9411764705882353, 0.5019607843137255, 0.5019607843137255),
	'lightcyan' : (0.8784313725490196, 1.0, 1.0),
	'lightgoldenrodyellow' : (0.9803921568627451, 0.9803921568627451, 0.8235294117647058),
	'lightgray' : (0.8274509803921568, 0.8274509803921568, 0.8274509803921568),
	'lightgreen' : (0.5647058823529412, 0.9333333333333333, 0.5647058823529412),
	'lightgrey' : (0.8274509803921568, 0.8274509803921568, 0.8274509803921568),
	'lightpink' : (1.0, 0.7137254901960784, 0.7568627450980392),
	'lightsalmon' : (1.0, 0.6274509803921569, 0.47843137254901963),
	'lightseagreen' : (0.12549019607843137, 0.6980392156862745, 0.6666666666666666),
	'lightskyblue' : (0.5294117647058824, 0.807843137254902, 0.9803921568627451),
	'lightslategray' : (0.4666666666666667, 0.5333333333333333, 0.6),
	'lightsteelblue' : (0.6901960784313725, 0.7686274509803922, 0.8705882352941177),
	'lightyellow' : (1.0, 1.0, 0.8784313725490196),
	'lime' : (0.0, 1.0, 0.0),
	'limegreen' : (0.19607843137254902, 0.803921568627451, 0.19607843137254902),
	'linen' : (0.9803921568627451, 0.9411764705882353, 0.9019607843137255),
	'magenta' : (1.0, 0.0, 1.0),
	'maroon' : (0.5019607843137255, 0.0, 0.0),
	'mediumaquamarine' : (0.4, 0.803921568627451, 0.6666666666666666),
	'mediumblue' : (0.0, 0.0, 0.803921568627451),
	'mediumorchid' : (0.7294117647058823, 0.3333333333333333, 0.8274509803921568),
	'mediumpurple' : (0.5764705882352941, 0.4392156862745098, 0.8588235294117647),
	'mediumseagreen' : (0.23529411764705882, 0.7019607843137254, 0.44313725490196076),
	'mediumslateblue' : (0.4823529411764706, 0.40784313725490196, 0.9333333333333333),
	'mediumspringgreen' : (0.0, 0.9803921568627451, 0.6039215686274509),
	'mediumturquoise' : (0.2823529411764706, 0.8196078431372549, 0.8),
	'mediumvioletred' : (0.7803921568627451, 0.08235294117647059, 0.5215686274509804),
	'midnightblue' : (0.09803921568627451, 0.09803921568627451, 0.4392156862745098),
	'mintcream' : (0.9607843137254902, 1.0, 0.9803921568627451),
	'mistyrose' : (1.0, 0.8941176470588236, 0.8823529411764706),
	'moccasin' : (1.0, 0.8941176470588236, 0.7098039215686275),
	'navajowhite' : (1.0, 0.8705882352941177, 0.6784313725490196),
	'navy' : (0.0, 0.0, 0.5019607843137255),
	'oldlace' : (0.9921568627450981, 0.9607843137254902, 0.9019607843137255),
	'olive' : (0.5019607843137255, 0.5019607843137255, 0.0),
	'olivedrab' : (0.4196078431372549, 0.5568627450980392, 0.13725490196078433),
	'orange' : (1.0, 0.6470588235294118, 0.0),
	'orangered' : (1.0, 0.27058823529411763, 0.0),
	'orchid' : (0.8549019607843137, 0.4392156862745098, 0.8392156862745098),
	'palegoldenrod' : (0.9333333333333333, 0.9098039215686274, 0.6666666666666666),
	'palegreen' : (0.596078431372549, 0.984313725490196, 0.596078431372549),
	'paleturquoise' : (0.6862745098039216, 0.9333333333333333, 0.9333333333333333),
	'palevioletred' : (0.8588235294117647, 0.4392156862745098, 0.5764705882352941),
	'papayawhip' : (1.0, 0.9372549019607843, 0.8352941176470589),
	'peachpuff' : (1.0, 0.8549019607843137, 0.7254901960784313),
	'peru' : (0.803921568627451, 0.5215686274509804, 0.24705882352941178),
	'pink' : (1.0, 0.7529411764705882, 0.796078431372549),
	'plum' : (0.8666666666666667, 0.6274509803921569, 0.8666666666666667),
	'powderblue' : (0.6901960784313725, 0.8784313725490196, 0.9019607843137255),
	'purple' : (0.5019607843137255, 0.0, 0.5019607843137255),
	'red' : (1.0, 0.0, 0.0),
	'rosybrown' : (0.7372549019607844, 0.5607843137254902, 0.5607843137254902),
	'royalblue' : (0.2549019607843137, 0.4117647058823529, 0.8823529411764706),
	'saddlebrown' : (0.5450980392156862, 0.27058823529411763, 0.07450980392156863),
	'salmon' : (0.9803921568627451, 0.5019607843137255, 0.4470588235294118),
	'sandybrown' : (0.9568627450980393, 0.6431372549019608, 0.3764705882352941),
	'seagreen' : (0.1803921568627451, 0.5450980392156862, 0.3411764705882353),
	'seashell' : (1.0, 0.9607843137254902, 0.9333333333333333),
	'sienna' : (0.6274509803921569, 0.3215686274509804, 0.17647058823529413),
	'silver' : (0.7529411764705882, 0.7529411764705882, 0.7529411764705882),
	'skyblue' : (0.5294117647058824, 0.807843137254902, 0.9215686274509803),
	'slateblue' : (0.41568627450980394, 0.35294117647058826, 0.803921568627451),
	'slategray' : (0.4392156862745098, 0.5019607843137255, 0.5647058823529412),
	'snow' : (1.0, 0.9803921568627451, 0.9803921568627451),
	'springgreen' : (0.0, 1.0, 0.4980392156862745),
	'steelblue' : (0.27450980392156865, 0.5098039215686274, 0.7058823529411765),
	'tan' : (0.8235294117647058, 0.7058823529411765, 0.5490196078431373),
	'teal' : (0.0, 0.5019607843137255, 0.5019607843137255),
	'thistle' : (0.8470588235294118, 0.7490196078431373, 0.8470588235294118),
	'tomato' : (1.0, 0.38823529411764707, 0.2784313725490196),
	'turquoise' : (0.25098039215686274, 0.8784313725490196, 0.8156862745098039),
	'violet' : (0.9333333333333333, 0.5098039215686274, 0.9333333333333333),
	'wheat' : (0.9607843137254902, 0.8705882352941177, 0.7019607843137254),
	'white' : (1.0, 1.0, 1.0),
	'whitesmoke' : (0.9607843137254902, 0.9607843137254902, 0.9607843137254902),
	'yellow' : (1.0, 1.0, 0.0),
	'yellowgreen' : (0.6039215686274509, 0.803921568627451, 0.19607843137254902)
}


colors4 = {
	'aliceblue' : (0.9411764705882353, 0.9725490196078431, 1.0, 1.),
	'antiquewhite' : (0.9803921568627451, 0.9215686274509803, 0.8431372549019608, 1.),
	'aqua' : (0.0, 1.0, 1.0, 1.),
	'aquamarine' : (0.4980392156862745, 1.0, 0.8313725490196079, 1.),
	'azure' : (0.9411764705882353, 1.0, 1.0, 1.),
	'beige' : (0.9607843137254902, 0.9607843137254902, 0.8627450980392157, 1.),
	'bisque' : (1.0, 0.8941176470588236, 0.7686274509803922, 1.),
	'black' : (0.0, 0.0, 0.0, 1.),
	'blanchedalmond' : (1.0, 0.9215686274509803, 0.803921568627451, 1.),
	'blue' : (0.0, 0.0, 1.0, 1.),
	'blueviolet' : (0.5411764705882353, 0.16862745098039217, 0.8862745098039215, 1.),
	'brown' : (0.6470588235294118, 0.16470588235294117, 0.16470588235294117, 1.),
	'burlywood' : (0.8705882352941177, 0.7215686274509804, 0.5294117647058824, 1.),
	'cadetblue' : (0.37254901960784315, 0.6196078431372549, 0.6274509803921569, 1.),
	'chartreuse' : (0.4980392156862745, 1.0, 0.0, 1.),
	'chocolate' : (0.8235294117647058, 0.4117647058823529, 0.11764705882352941, 1.),
	'coral' : (1.0, 0.4980392156862745, 0.3137254901960784, 1.),
	'cornflowerblue' : (0.39215686274509803, 0.5843137254901961, 0.9294117647058824, 1.),
	'cornsilk' : (1.0, 0.9725490196078431, 0.8627450980392157, 1.),
	'crimson' : (0.8627450980392157, 0.0784313725490196, 0.23529411764705882, 1.),
	'cyan' : (0.0, 1.0, 1.0, 1.),
	'darkblue' : (0.0, 0.0, 0.5450980392156862, 1.),
	'darkcyan' : (0.0, 0.5450980392156862, 0.5450980392156862, 1.),
	'darkgoldenrod' : (0.7215686274509804, 0.5254901960784314, 0.043137254901960784, 1.),
	'darkgray' : (0.6627450980392157, 0.6627450980392157, 0.6627450980392157, 1.),
	'darkgreen' : (0.0, 0.39215686274509803, 0.0, 1.),
	'darkgrey' : (0.6627450980392157, 0.6627450980392157, 0.6627450980392157, 1.),
	'darkkhaki' : (0.7411764705882353, 0.7176470588235294, 0.4196078431372549, 1.),
	'darkmagenta' : (0.5450980392156862, 0.0, 0.5450980392156862, 1.),
	'darkolivegreen' : (0.3333333333333333, 0.4196078431372549, 0.1843137254901961, 1.),
	'darkorange' : (1.0, 0.5490196078431373, 0.0, 1.),
	'darkorchid' : (0.6, 0.19607843137254902, 0.8, 1.),
	'darkred' : (0.5450980392156862, 0.0, 0.0, 1.),
	'darksalmon' : (0.9137254901960784, 0.5882352941176471, 0.47843137254901963, 1.),
	'darkseagreen' : (0.5607843137254902, 0.7372549019607844, 0.5607843137254902, 1.),
	'darkslateblue' : (0.2823529411764706, 0.23921568627450981, 0.5450980392156862, 1.),
	'darkslategray' : (0.1843137254901961, 0.30980392156862746, 0.30980392156862746, 1.),
	'darkturquoise' : (0.0, 0.807843137254902, 0.8196078431372549, 1.),
	'darkviolet' : (0.5803921568627451, 0.0, 0.8274509803921568, 1.),
	'deeppink' : (1.0, 0.0784313725490196, 0.5764705882352941, 1.),
	'deepskyblue' : (0.0, 0.7490196078431373, 1.0, 1.),
	'dimgray' : (0.4117647058823529, 0.4117647058823529, 0.4117647058823529, 1.),
	'dodgerblue' : (0.11764705882352941, 0.5647058823529412, 1.0, 1.),
	'firebrick' : (0.6980392156862745, 0.13333333333333333, 0.13333333333333333, 1.),
	'floralwhite' : (1.0, 0.9803921568627451, 0.9411764705882353, 1.),
	'forestgreen' : (0.13333333333333333, 0.5450980392156862, 0.13333333333333333, 1.),
	'gainsboro' : (0.8627450980392157, 0.8627450980392157, 0.8627450980392157, 1.),
	'ghostwhite' : (0.9725490196078431, 0.9725490196078431, 1.0, 1.),
	'gold' : (1.0, 0.8431372549019608, 0.0, 1.),
	'goldenrod' : (0.8549019607843137, 0.6470588235294118, 0.12549019607843137, 1.),
	'gray' : (0.5019607843137255, 0.5019607843137255, 0.5019607843137255, 1.),
	'green' : (0.0, 0.5019607843137255, 0.0, 1.),
	'greenyellow' : (0.6784313725490196, 1.0, 0.1843137254901961, 1.),
	'grey' : (0.5019607843137255, 0.5019607843137255, 0.5019607843137255, 1.),
	'honeydew' : (0.9411764705882353, 1.0, 0.9411764705882353, 1.),
	'hotpink' : (1.0, 0.4117647058823529, 0.7058823529411765, 1.),
	'indianred' : (0.803921568627451, 0.3607843137254902, 0.3607843137254902, 1.),
	'indigo' : (0.29411764705882354, 0.0, 0.5098039215686274, 1.),
	'ivory' : (1.0, 1.0, 0.9411764705882353, 1.),
	'khaki' : (0.9411764705882353, 0.9019607843137255, 0.5490196078431373, 1.),
	'lavender' : (0.9019607843137255, 0.9019607843137255, 0.9803921568627451, 1.),
	'lavenderblush' : (1.0, 0.9411764705882353, 0.9607843137254902, 1.),
	'lawngreen' : (0.48627450980392156, 0.9882352941176471, 0.0, 1.),
	'lemonchiffon' : (1.0, 0.9803921568627451, 0.803921568627451, 1.),
	'lightblue' : (0.6784313725490196, 0.8470588235294118, 0.9019607843137255, 1.),
	'lightcoral' : (0.9411764705882353, 0.5019607843137255, 0.5019607843137255, 1.),
	'lightcyan' : (0.8784313725490196, 1.0, 1.0, 1.),
	'lightgoldenrodyellow' : (0.9803921568627451, 0.9803921568627451, 0.8235294117647058, 1.),
	'lightgray' : (0.8274509803921568, 0.8274509803921568, 0.8274509803921568, 1.),
	'lightgreen' : (0.5647058823529412, 0.9333333333333333, 0.5647058823529412, 1.),
	'lightgrey' : (0.8274509803921568, 0.8274509803921568, 0.8274509803921568, 1.),
	'lightpink' : (1.0, 0.7137254901960784, 0.7568627450980392, 1.),
	'lightsalmon' : (1.0, 0.6274509803921569, 0.47843137254901963, 1.),
	'lightseagreen' : (0.12549019607843137, 0.6980392156862745, 0.6666666666666666, 1.),
	'lightskyblue' : (0.5294117647058824, 0.807843137254902, 0.9803921568627451, 1.),
	'lightslategray' : (0.4666666666666667, 0.5333333333333333, 0.6, 1.),
	'lightsteelblue' : (0.6901960784313725, 0.7686274509803922, 0.8705882352941177, 1.),
	'lightyellow' : (1.0, 1.0, 0.8784313725490196, 1.),
	'lime' : (0.0, 1.0, 0.0, 1.),
	'limegreen' : (0.19607843137254902, 0.803921568627451, 0.19607843137254902, 1.),
	'linen' : (0.9803921568627451, 0.9411764705882353, 0.9019607843137255, 1.),
	'magenta' : (1.0, 0.0, 1.0, 1.),
	'maroon' : (0.5019607843137255, 0.0, 0.0, 1.),
	'mediumaquamarine' : (0.4, 0.803921568627451, 0.6666666666666666, 1.),
	'mediumblue' : (0.0, 0.0, 0.803921568627451, 1.),
	'mediumorchid' : (0.7294117647058823, 0.3333333333333333, 0.8274509803921568, 1.),
	'mediumpurple' : (0.5764705882352941, 0.4392156862745098, 0.8588235294117647, 1.),
	'mediumseagreen' : (0.23529411764705882, 0.7019607843137254, 0.44313725490196076, 1.),
	'mediumslateblue' : (0.4823529411764706, 0.40784313725490196, 0.9333333333333333, 1.),
	'mediumspringgreen' : (0.0, 0.9803921568627451, 0.6039215686274509, 1.),
	'mediumturquoise' : (0.2823529411764706, 0.8196078431372549, 0.8, 1.),
	'mediumvioletred' : (0.7803921568627451, 0.08235294117647059, 0.5215686274509804, 1.),
	'midnightblue' : (0.09803921568627451, 0.09803921568627451, 0.4392156862745098, 1.),
	'mintcream' : (0.9607843137254902, 1.0, 0.9803921568627451, 1.),
	'mistyrose' : (1.0, 0.8941176470588236, 0.8823529411764706, 1.),
	'moccasin' : (1.0, 0.8941176470588236, 0.7098039215686275, 1.),
	'navajowhite' : (1.0, 0.8705882352941177, 0.6784313725490196, 1.),
	'navy' : (0.0, 0.0, 0.5019607843137255, 1.),
	'oldlace' : (0.9921568627450981, 0.9607843137254902, 0.9019607843137255, 1.),
	'olive' : (0.5019607843137255, 0.5019607843137255, 0.0, 1.),
	'olivedrab' : (0.4196078431372549, 0.5568627450980392, 0.13725490196078433, 1.),
	'orange' : (1.0, 0.6470588235294118, 0.0, 1.),
	'orangered' : (1.0, 0.27058823529411763, 0.0, 1.),
	'orchid' : (0.8549019607843137, 0.4392156862745098, 0.8392156862745098, 1.),
	'palegoldenrod' : (0.9333333333333333, 0.9098039215686274, 0.6666666666666666, 1.),
	'palegreen' : (0.596078431372549, 0.984313725490196, 0.596078431372549, 1.),
	'paleturquoise' : (0.6862745098039216, 0.9333333333333333, 0.9333333333333333, 1.),
	'palevioletred' : (0.8588235294117647, 0.4392156862745098, 0.5764705882352941, 1.),
	'papayawhip' : (1.0, 0.9372549019607843, 0.8352941176470589, 1.),
	'peachpuff' : (1.0, 0.8549019607843137, 0.7254901960784313, 1.),
	'peru' : (0.803921568627451, 0.5215686274509804, 0.24705882352941178, 1.),
	'pink' : (1.0, 0.7529411764705882, 0.796078431372549, 1.),
	'plum' : (0.8666666666666667, 0.6274509803921569, 0.8666666666666667, 1.),
	'powderblue' : (0.6901960784313725, 0.8784313725490196, 0.9019607843137255, 1.),
	'purple' : (0.5019607843137255, 0.0, 0.5019607843137255, 1.),
	'red' : (1.0, 0.0, 0.0, 1.),
	'rosybrown' : (0.7372549019607844, 0.5607843137254902, 0.5607843137254902, 1.),
	'royalblue' : (0.2549019607843137, 0.4117647058823529, 0.8823529411764706, 1.),
	'saddlebrown' : (0.5450980392156862, 0.27058823529411763, 0.07450980392156863, 1.),
	'salmon' : (0.9803921568627451, 0.5019607843137255, 0.4470588235294118, 1.),
	'sandybrown' : (0.9568627450980393, 0.6431372549019608, 0.3764705882352941, 1.),
	'seagreen' : (0.1803921568627451, 0.5450980392156862, 0.3411764705882353, 1.),
	'seashell' : (1.0, 0.9607843137254902, 0.9333333333333333, 1.),
	'sienna' : (0.6274509803921569, 0.3215686274509804, 0.17647058823529413, 1.),
	'silver' : (0.7529411764705882, 0.7529411764705882, 0.7529411764705882, 1.),
	'skyblue' : (0.5294117647058824, 0.807843137254902, 0.9215686274509803, 1.),
	'slateblue' : (0.41568627450980394, 0.35294117647058826, 0.803921568627451, 1.),
	'slategray' : (0.4392156862745098, 0.5019607843137255, 0.5647058823529412, 1.),
	'snow' : (1.0, 0.9803921568627451, 0.9803921568627451, 1.),
	'springgreen' : (0.0, 1.0, 0.4980392156862745, 1.),
	'steelblue' : (0.27450980392156865, 0.5098039215686274, 0.7058823529411765, 1.),
	'tan' : (0.8235294117647058, 0.7058823529411765, 0.5490196078431373, 1.),
	'teal' : (0.0, 0.5019607843137255, 0.5019607843137255, 1.),
	'thistle' : (0.8470588235294118, 0.7490196078431373, 0.8470588235294118, 1.),
	'tomato' : (1.0, 0.38823529411764707, 0.2784313725490196, 1.),
	'turquoise' : (0.25098039215686274, 0.8784313725490196, 0.8156862745098039, 1.),
	'violet' : (0.9333333333333333, 0.5098039215686274, 0.9333333333333333, 1.),
	'wheat' : (0.9607843137254902, 0.8705882352941177, 0.7019607843137254, 1.),
	'white' : (1.0, 1.0, 1.0, 1.),
	'whitesmoke' : (0.9607843137254902, 0.9607843137254902, 0.9607843137254902, 1.),
	'yellow' : (1.0, 1.0, 0.0, 1.),
	'yellowgreen' : (0.6039215686274509, 0.803921568627451, 0.19607843137254902, 1.)
}


class Material:
	def __init__(self, amb=colors4['white'], dif=colors4['white'], spec=colors4['white'], shine=1.):
		self.ambient = amb
		self.diffuse = dif
		self.specular = spec
		self.shiny   = shine


	def set(self):
		glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, self.ambient)
		glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, self.diffuse)
		glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, self.specular)
		glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, self.shiny)


materials = {
	"emerald" 	: Material((0.0215,0.1745,0.0215,1.),	(0.07568,0.61424,0.07568,1.),	(0.633,0.727811,0.633,1.),	76.8),
	"jade" 		: Material((0.135,0.2225,0.1575,1.),	(0.54,0.89,0.63,1.),	(0.316228,0.316228,0.316228,1.),	12.8),
	"obsidian" 	: Material((0.05375,0.05,0.06625,1.),	(0.18275,0.17,0.22525,1.),	(0.332741,0.328634,0.346435,1.),	38.4),
	"pearl" 	: Material((0.25,0.20725,0.20725,1.),	(1,0.829,0.829,1.),	(0.296648,0.296648,0.296648,1.),	11.264),
	"ruby" 		: Material((0.1745,0.01175,0.01175,1.),	(0.61424,0.04136,0.04136,1.),	(0.727811,0.626959,0.626959,1.),	76.8),
	"turquoise" : Material((0.1,0.18725,0.1745,1.),	(0.396,0.74151,0.69102,1.),	(0.297254,0.30829,0.306678,1.),	12.8),
	"brass" 	: Material((0.329412,0.223529,0.027451,1.),	(0.780392,0.568627,0.113725,1.),	(0.992157,0.941176,0.807843,1.),	27.89743616),
	"bronze" 	: Material((0.2125,0.1275,0.054,1.),	(0.714,0.4284,0.18144,1.),	(0.393548,0.271906,0.166721,1.),	25.6),
	"chrome" 	: Material((0.25,0.25,0.25,1.),	(0.4,0.4,0.4,1.),	(0.774597,0.774597,0.774597,1.),	76.8),
	"copper" 	: Material((0.19125,0.0735,0.0225,1.),	(0.7038,0.27048,0.0828,1.),	(0.256777,0.137622,0.086014,1.),	12.8),
	"gold" 		: Material((0.24725,0.1995,0.0745,1.),	(0.75164,0.60648,0.22648,1.),	(0.628281,0.555802,0.366065,1.),	51.2),
	"silver" 	: Material((0.19225,0.19225,0.19225,1.),	(0.50754,0.50754,0.50754,1.),	(0.508273,0.508273,0.508273,1.),	51.2),
	"blackplastic" 	: Material((0,0,0,1.),	(0.01,0.01,0.01,1.),	(0.5,0.5,0.5,1.),	32),
	"cyanplastic" 	: Material((0,0.1,0.06,1.),	(0,0.50980392,0.50980392,1.),	(0.50196078,0.50196078,0.50196078,1.),	32),
	"greenplastic" 	: Material((0,0,0,1.),	(0.1,0.35,0.1,1.),	(0.45,0.55,0.45,1.),	32),
	"redplastic" 	: Material((0,0,0,1.),	(0.5,0,0,1.),	(0.7,0.6,0.6,1.),	32),
	"whiteplastic" 	: Material((0,0,0,1.),	(0.55,0.55,0.55,1.),	(0.7,0.7,0.7,1.),	32),
	"yellowplastic" : Material((0,0,0,1.),	(0.5,0.5,0,1.),	(0.6,0.6,0.5,1.),	32),
	"blackrubber" 	: Material((0.02,0.02,0.02,1.),	(0.01,0.01,0.01,1.),	(0.4,0.4,0.4,1.),	10),
	"cyanrubber" 	: Material((0,0.05,0.05,1.),	(0.4,0.5,0.5,1.),	(0.04,0.7,0.7,1.),	10),
	"greenrubber" 	: Material((0,0.05,0,1.),	(0.4,0.5,0.4,1.),	(0.04,0.7,0.04,1.),	10),
	"redrubber" 	: Material((0.05,0,0,1.),	(0.5,0.4,0.4,1.),	(0.7,0.04,0.04,1.),	10),
	"whiterubber" 	: Material((0.05,0.05,0.05,1.),	(0.5,0.5,0.5,1.),	(0.7,0.7,0.7,1.),	10),
	"yellowrubber" 	: Material((0.05,0.05,0,1.),	(0.5,0.5,0.4,1.),	(0.7,0.7,0.04,1.),	10)
}

materialList = list(materials.keys())