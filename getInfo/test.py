#encoding:utf-8
from bs4 import BeautifulSoup
htmldoc = """


<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head id="ctl00_Head1"><title>
	三峡大学教务管理系统
</title><link href="../Images/Default.css" rel="stylesheet" type="text/css" />

<script language="javascript" type="text/javascript">
// <!CDATA[

function window_onkeydown() {
//window.alert(event.keyCode);
if ((event.altKey)||((event.keyCode==8)&&(event.srcElement.type!="text"&&event.srcElement.type!="textarea"&&event.srcElement.type!="password"))||((event.ctrlKey)&&((event.keyCode==78)||(event.keyCode==82)))||(event.keyCode==116))
{

event.keyCode=0;
event.returnValue=false;
}
}

// ]]>
</script>
<style type="text/css">
	.ctl00_Menu2_0 { background-color:white;visibility:hidden;display:none;position:absolute;left:0px;top:0px; }
	.ctl00_Menu2_1 { text-decoration:none; }
	.ctl00_Menu2_2 { background-color:Red; }
	.ctl00_Menu1_0 { background-color:white;visibility:hidden;display:none;position:absolute;left:0px;top:0px; }
	.ctl00_Menu1_1 { text-decoration:none; }
	.ctl00_Menu1_2 {  }

</style></head>
<body onkeydown="return window_onkeydown()">
    <form name="aspnetForm" method="post" action="Score_Query.aspx" id="aspnetForm">
<div>
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="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" />
</div>





        <div>
            <table width="100%" height="102" border="0" cellpadding="0" cellspacing="0">
                <tr>
                    <td class="topbj_bgimage">
                        <table width="100%" height="102" border="0" cellpadding="0" cellspacing="0">
                            <tr>
                                <td colspan="3" class="top1_bgimage" width="100%" height="71">
                                </td>
                            </tr>
                            <tr>
                                <td width="16%" class="top2_bgimage">
                                    <table width="100%" height="31" border="0" cellpadding="0" cellspacing="0">
                                        <tr>
                                            <td height="3">
                                            </td>
                                        </tr>
                                        <tr>
                                            <td align="left">
                                                &nbsp;&nbsp;&nbsp;&nbsp;『<span id="ctl00_lblSignIn">2012136121吴化吉</span>』
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                                <td align="left" class="top3_bgimage">
                                    <table width="100%" height="31" border="0" cellpadding="0" cellspacing="0">
                                        <tr>
                                            <td width="9%">
                                            </td>
                                            <td>
                                                <table height="31" border="0" cellpadding="0" cellspacing="0">

                                               <tr>
                                                        <td rowspan="2"  width="0" height="31">
                                                        </td>
                                                        <td height="8">
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td >
                                                            <a href="#ctl00_Menu2_SkipLink" style="display:inline-block;height:1px;width:1px;"><img src="/jwc_glxt/WebResource.axd?d=p-y_zQv1oWCYLLME-mCiOQ2&amp;t=634184281466406250" alt="Skip Navigation Links" style="border-width:0px;" /></a><div id="ctl00_Menu2">
	<span title="学业预警"><a class="ctl00_Menu2_1" href="javascript:__doPostBack('ctl00$Menu2','o学业预警')">学业预警<img src="/jwc_glxt/WebResource.axd?d=s6sDJEXkR4ATKAlea15GU041wWuBm3nobrglLZFzuMw1&amp;t=634184281466406250" alt="Expand 学业预警" align="absmiddle" style="border-width:0px;" /></a></span>
</div><a name="ctl00_Menu2_SkipLink"></a>

                                                          </td>
                                                          <td>
                                                          <a href="#ctl00_Menu1_SkipLink" style="display:inline-block;height:1px;width:1px;"><img src="/jwc_glxt/WebResource.axd?d=p-y_zQv1oWCYLLME-mCiOQ2&amp;t=634184281466406250" alt="Skip Navigation Links" style="border-width:0px;" /></a><div id="ctl00_Menu1">
	<span title="各类通知及事务"><a class="ctl00_Menu1_1" href="/jwc_glxt/Stu_Notice/Notice_Query.aspx"> | | 即时事务</a></span> <span title="学生选课"><a class="ctl00_Menu1_1" href="javascript:__doPostBack('ctl00$Menu1','o || || 学生选课')"> | | 学生选课<img src="/jwc_glxt/WebResource.axd?d=s6sDJEXkR4ATKAlea15GU041wWuBm3nobrglLZFzuMw1&amp;t=634184281466406250" alt="Expand  | | 学生选课" align="absmiddle" style="border-width:0px;" /></a></span> <span title="学生成绩查询"><a class="ctl00_Menu1_1" href="javascript:__doPostBack('ctl00$Menu1','o || || 成绩查询')"> | | 成绩查询<img src="/jwc_glxt/WebResource.axd?d=s6sDJEXkR4ATKAlea15GU041wWuBm3nobrglLZFzuMw1&amp;t=634184281466406250" alt="Expand  | | 成绩查询" align="absmiddle" style="border-width:0px;" /></a></span> <span title="各类报名"><a class="ctl00_Menu1_1" href="javascript:__doPostBack('ctl00$Menu1','o || || 各类报名')"> | | 各类报名<img src="/jwc_glxt/WebResource.axd?d=s6sDJEXkR4ATKAlea15GU041wWuBm3nobrglLZFzuMw1&amp;t=634184281466406250" alt="Expand  | | 各类报名" align="absmiddle" style="border-width:0px;" /></a></span> <span title="学生评教"><a class="ctl00_Menu1_1" href="/jwc_glxt/Stu_Assess/Stu_Assess.aspx"> | | 学生评教</a></span> <span title="个人信息"><a class="ctl00_Menu1_1" href="javascript:__doPostBack('ctl00$Menu1','o || || 个人信息')"> | | 个人信息<img src="/jwc_glxt/WebResource.axd?d=s6sDJEXkR4ATKAlea15GU041wWuBm3nobrglLZFzuMw1&amp;t=634184281466406250" alt="Expand  | | 个人信息" align="absmiddle" style="border-width:0px;" /></a></span>
</div><a name="ctl00_Menu1_SkipLink"></a>
                                                        </td>
                                                    </tr>
                                                </table>
                                            </td>
                                            <td>
                                                <table height="31" border="0" cellpadding="0" cellspacing="0">
                                                    <tr>
                                                        <td rowspan="2"  width="0" height="31">
                                                        </td>
                                                        <td height="8">
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td>
                                                        </td>
                                                    </tr>
                                                </table>
                                            </td>
                                            <td>
                                                <table height="31" border="0" cellpadding="0" cellspacing="0">
                                                    <tr>
                                                        <td rowspan="2" class="top4_bgimage" width="39" height="31">
                                                        </td>
                                                        <td height="8" width="60">
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td align="center">
                                                            <a href="../Login.aspx?xttc=1" target="_top">退出</a>
                                                        </td>
                                                    </tr>
                                                </table>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                                <td width="6%" class="top5_bgimage" height="31">
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
        </div>
        <div style="text-align: center" class="table_bgcolor">
            <div  style="width: 96%" >


    <table class="table_bordercolor" border="1" cellpadding="1" cellspacing="0" style="height: 25px;width: 100%">
     <caption><h2>学生个人成绩查询</h2></caption>
        <tr>
            <td class="table_titlebgcolor">
                学年：<select name="ctl00$MainContentPlaceHolder$School_Year" id="ctl00_MainContentPlaceHolder_School_Year" ValueField="Value" TextField="Text" style="border-style:Groove;">
	<option selected="selected" value="0">(不填)</option>
	<option value="2021">2021</option>
	<option value="2020">2020</option>
	<option value="2019">2019</option>
	<option value="2018">2018</option>
	<option value="2017">2017</option>
	<option value="2016">2016</option>
	<option value="2015">2015</option>
	<option value="2014">2014</option>
	<option value="2013">2013</option>
	<option value="2012">2012</option>
	<option value="2011">2011</option>
	<option value="2010">2010</option>
	<option value="2009">2009</option>
	<option value="2008">2008</option>
	<option value="2007">2007</option>
	<option value="2006">2006</option>
	<option value="2005">2005</option>
	<option value="2004">2004</option>
	<option value="2003">2003</option>
	<option value="2002">2002</option>
	<option value="2001">2001</option>
	<option value="2000">2000</option>
	<option value="1999">1999</option>
	<option value="1998">1998</option>
	<option value="1997">1997</option>
	<option value="1996">1996</option>

</select>&nbsp;&nbsp;
                学期：<select name="ctl00$MainContentPlaceHolder$School_Term" id="ctl00_MainContentPlaceHolder_School_Term" ValueField="Value" TextField="Text" style="border-style:Groove;width:100px;">
	<option selected="selected" value="0">(不填)</option>
	<option value="1">春季学期</option>
	<option value="2">夏季学期</option>
	<option value="3">秋季学期</option>
	<option value="4">冬季学期</option>

</select>
                &nbsp;&nbsp;
                排序方式：
                <input id="ctl00_MainContentPlaceHolder_RadioButton1" type="radio" name="ctl00$MainContentPlaceHolder$score_q" value="RadioButton1" /><label for="ctl00_MainContentPlaceHolder_RadioButton1">按学年学期</label>
                <input id="ctl00_MainContentPlaceHolder_RadioButton2" type="radio" name="ctl00$MainContentPlaceHolder$score_q" value="RadioButton2" checked="checked" /><label for="ctl00_MainContentPlaceHolder_RadioButton2">按所学课程</label>&nbsp;&nbsp;
                <input id="ctl00_MainContentPlaceHolder_CheckBox1" type="checkbox" name="ctl00$MainContentPlaceHolder$CheckBox1" /><label for="ctl00_MainContentPlaceHolder_CheckBox1">显示绩点</label>
                <input type="image" name="ctl00$MainContentPlaceHolder$BtnSearch" id="ctl00_MainContentPlaceHolder_BtnSearch" src="../images/button_search.GIF" style="border-width:0px;" />
            </td>
            </tr>
            <tr>
            <td align="center"><font color="red">注意：若查询不到某门课程的成绩，请检查该门课程是否已进行评教</font></td>
        </tr>
    </table>

    <div>
	<table class="GridViewStyle" cellspacing="0" rules="all" border="1" id="ctl00_MainContentPlaceHolder_GridScore" style="border-collapse:collapse;">
		<caption>
			(共95条/1页)
		</caption><tr class="HeaderStyle">
			<th scope="col">学年</th><th scope="col">学期</th><th scope="col">课程名称</th><th scope="col">课程学分</th><th scope="col">考试类型</th><th scope="col">考试成绩</th><th scope="col">所获学分</th>
		</tr><tr>
			<td>2012</td><td>3</td><td>电路与模拟电子技术</td><td>4.5</td><td>正常</td><td>35</td><td>0</td>
		</tr><tr>
			<td>2012</td><td>3</td><td>电路与模拟电子技术</td><td>4.5</td><td>补考</td><td>6</td><td>0</td>
		</tr><tr>
			<td>2014</td><td>1</td><td>电路与模拟电子技术</td><td>4.5</td><td>正常</td><td>65</td><td>4.5</td>
		</tr><tr>
			<td>2012</td><td>3</td><td>电路与模拟电子技术实验</td><td>1</td><td>正常</td><td>良</td><td>1</td>
		</tr><tr>
			<td>2012</td><td>3</td><td>高等数学Ⅰ(一)</td><td>5.5</td><td>正常</td><td>68</td><td>5.5</td>
		</tr><tr>
			<td>2013</td><td>1</td><td>高等数学Ⅰ(二)</td><td>5.5</td><td>正常</td><td>60</td><td>5.5</td>
		</tr><tr>
			<td>2013</td><td>1</td><td>线性代数Ⅰ</td><td>2</td><td>正常</td><td>69</td><td>2</td>
		</tr><tr>
			<td>2013</td><td>3</td><td>概率统计Ⅰ</td><td>2.5</td><td>正常</td><td>62</td><td>2.5</td>
		</tr><tr>
			<td>2013</td><td>1</td><td>大学物理Ⅰ(一)</td><td>3.5</td><td>正常</td><td>61</td><td>3.5</td>
		</tr><tr>
			<td>2013</td><td>3</td><td>大学物理Ⅰ(二)</td><td>3</td><td>正常</td><td>65</td><td>3</td>
		</tr><tr>
			<td>2013</td><td>1</td><td>物理实验Ⅰ(一)</td><td>1.5</td><td>正常</td><td>80</td><td>1.5</td>
		</tr><tr>
			<td>2013</td><td>3</td><td>物理实验Ⅰ(二)</td><td>1.5</td><td>正常</td><td>40</td><td>0</td>
		</tr><tr>
			<td>2013</td><td>3</td><td>物理实验Ⅰ(二)</td><td>1.5</td><td>补考</td><td>60</td><td>1.5</td>
		</tr><tr>
			<td>2014</td><td>1</td><td>数学建模</td><td>2</td><td>正常</td><td>81</td><td>2</td>
		</tr><tr>
			<td>2013</td><td>1</td><td>数学建模</td><td>2</td><td>正常</td><td>86</td><td>2</td>
		</tr><tr>
			<td>2012</td><td>3</td><td>体育</td><td>1</td><td>正常</td><td>合格</td><td>1</td>
		</tr><tr>
			<td>2013</td><td>1</td><td>体育</td><td>1</td><td>正常</td><td>合格</td><td>1</td>
		</tr><tr>
			<td>2013</td><td>3</td><td>体育</td><td>1</td><td>正常</td><td>79</td><td>1</td>
		</tr><tr>
			<td>2014</td><td>1</td><td>体育</td><td>1</td><td>正常</td><td>65</td><td>1</td>
		</tr><tr>
			<td>2012</td><td>3</td><td>计算机基础</td><td>3</td><td>正常</td><td>84</td><td>3</td>
		</tr><tr>
			<td>2012</td><td>3</td><td>C语言程序设计</td><td>4</td><td>正常</td><td>60</td><td>4</td>
		</tr><tr>
			<td>2015</td><td>1</td><td>计算机网络</td><td>3</td><td>正常</td><td>66</td><td>3</td>
		</tr><tr>
			<td>2013</td><td>3</td><td>面向对象程序设计(C  )</td><td>2</td><td>正常</td><td>71</td><td>2</td>
		</tr><tr>
			<td>2015</td><td>1</td><td>嵌入式系统原理与设计</td><td>2.5</td><td>正常</td><td>73</td><td>2.5</td>
		</tr><tr>
			<td>2013</td><td>1</td><td>数据结构</td><td>2</td><td>正常</td><td>41</td><td>0</td>
		</tr><tr>
			<td>2013</td><td>1</td><td>数据结构</td><td>2</td><td>补考</td><td>16</td><td>0</td>
		</tr><tr>
			<td>2014</td><td>3</td><td>数字图像处理</td><td>2</td><td>正常</td><td>83</td><td>2</td>
		</tr><tr>
			<td>2014</td><td>1</td><td>随机信号分析</td><td>2</td><td>正常</td><td>63</td><td>2</td>
		</tr><tr>
			<td>2014</td><td>3</td><td>通信原理Ⅰ</td><td>4.5</td><td>正常</td><td>42</td><td>0</td>
		</tr><tr>
			<td>2014</td><td>3</td><td>通信原理Ⅰ</td><td>4.5</td><td>补考</td><td>60</td><td>4.5</td>
		</tr><tr>
			<td>2013</td><td>3</td><td>微波技术与天线</td><td>2</td><td>正常</td><td>80</td><td>2</td>
		</tr><tr>
			<td>2013</td><td>3</td><td>微型计算机技术</td><td>4</td><td>正常</td><td>33</td><td>0</td>
		</tr><tr>
			<td>2013</td><td>3</td><td>微型计算机技术</td><td>4</td><td>补考</td><td>60</td><td>4</td>
		</tr><tr>
			<td>2015</td><td>1</td><td>现代交换原理</td><td>2.5</td><td>正常</td><td>66</td><td>2.5</td>
		</tr><tr>
			<td>2013</td><td>3</td><td>信号与系统</td><td>4.5</td><td>正常</td><td>27</td><td>0</td>
		</tr><tr>
			<td>2013</td><td>3</td><td>信号与系统</td><td>4.5</td><td>补考</td><td>23</td><td>0</td>
		</tr><tr>
			<td>2015</td><td>1</td><td>移动通信</td><td>3</td><td>正常</td><td>54</td><td>0</td>
		</tr><tr>
			<td>2015</td><td>1</td><td>移动通信</td><td>3</td><td>补考</td><td>60</td><td>3</td>
		</tr><tr>
			<td>2015</td><td>1</td><td>通信工程概预算</td><td>0.5</td><td>正常</td><td>80</td><td>0.5</td>
		</tr><tr>
			<td>2014</td><td>3</td><td>通信电源</td><td>2</td><td>正常</td><td>85</td><td>2</td>
		</tr><tr>
			<td>2015</td><td>1</td><td>无线网络规划与优化</td><td>2</td><td>正常</td><td>85</td><td>2</td>
		</tr><tr>
			<td>2012</td><td>3</td><td>通信工程学科概论(双语)</td><td>0.5</td><td>正常</td><td>94</td><td>0.5</td>
		</tr><tr>
			<td>2014</td><td>3</td><td>传感器与检测技术</td><td>1.5</td><td>正常</td><td>70</td><td>1.5</td>
		</tr><tr>
			<td>2014</td><td>1</td><td>通信电子线路</td><td>2.5</td><td>正常</td><td>43</td><td>0</td>
		</tr><tr>
			<td>2014</td><td>1</td><td>通信电子线路</td><td>2.5</td><td>补考</td><td>60</td><td>2.5</td>
		</tr><tr>
			<td>2014</td><td>1</td><td>数字信号处理</td><td>3</td><td>正常</td><td>41</td><td>0</td>
		</tr><tr>
			<td>2014</td><td>1</td><td>数字信号处理</td><td>3</td><td>补考</td><td>60</td><td>3</td>
		</tr><tr>
			<td>2013</td><td>3</td><td>电磁场与电磁波</td><td>2.5</td><td>正常</td><td>61</td><td>2.5</td>
		</tr><tr>
			<td>2014</td><td>3</td><td>射频电路分析</td><td>2</td><td>正常</td><td>61</td><td>2</td>
		</tr><tr>
			<td>2013</td><td>1</td><td>Multisim电子技术设计</td><td>1</td><td>正常</td><td>89</td><td>1</td>
		</tr><tr>
			<td>2014</td><td>1</td><td>信息论基础</td><td>2.5</td><td>正常</td><td>87</td><td>2.5</td>
		</tr><tr>
			<td>2015</td><td>1</td><td>通信科技英语</td><td>1</td><td>正常</td><td>85</td><td>1</td>
		</tr><tr>
			<td>2015</td><td>1</td><td>(研讨)通信前沿技术</td><td>1</td><td>正常</td><td>89</td><td>1</td>
		</tr><tr>
			<td>2014</td><td>3</td><td>FPGA与通信系统设计</td><td>1</td><td>正常</td><td>82</td><td>1</td>
		</tr><tr>
			<td>2015</td><td>1</td><td>数据结构III</td><td>2</td><td>正常</td><td>76</td><td>2</td>
		</tr><tr>
			<td>2014</td><td>3</td><td>脉冲与数字电路</td><td>3</td><td>正常</td><td>60</td><td>3</td>
		</tr><tr>
			<td>2014</td><td>3</td><td>通信原理实验</td><td>0.5</td><td>正常</td><td>81</td><td>0.5</td>
		</tr><tr>
			<td>2015</td><td>1</td><td>Protel与电子系统课程设计</td><td>2</td><td>正常</td><td>80</td><td>2</td>
		</tr><tr>
			<td>2014</td><td>3</td><td>DSP系统课程设计</td><td>1</td><td>正常</td><td>92</td><td>1</td>
		</tr><tr>
			<td>2014</td><td>3</td><td>数字通信系统课程设计</td><td>1</td><td>正常</td><td>82</td><td>1</td>
		</tr><tr>
			<td>2014</td><td>1</td><td>通信电子线路测量与实验</td><td>1</td><td>正常</td><td>78</td><td>1</td>
		</tr><tr>
			<td>2013</td><td>1</td><td>数字电路与逻辑设计</td><td>3</td><td>正常</td><td>24</td><td>0</td>
		</tr><tr>
			<td>2013</td><td>1</td><td>数字电路与逻辑设计</td><td>3</td><td>补考</td><td>7</td><td>0</td>
		</tr><tr>
			<td>2015</td><td>1</td><td>项目综合实践1</td><td>2</td><td>正常</td><td>90</td><td>2</td>
		</tr><tr>
			<td>2013</td><td>1</td><td>FPGA与数字逻辑课程设计</td><td>1.5</td><td>正常</td><td>82</td><td>1.5</td>
		</tr><tr>
			<td>2013</td><td>3</td><td>AVR单片机应用课程设计</td><td>3</td><td>正常</td><td>81</td><td>3</td>
		</tr><tr>
			<td>2014</td><td>1</td><td>MATLAB与信号处理课程设计</td><td>1</td><td>正常</td><td>91</td><td>1</td>
		</tr><tr>
			<td>2014</td><td>1</td><td>电子线路课程设计(低、高频)</td><td>1</td><td>正常</td><td>75</td><td>1</td>
		</tr><tr>
			<td>2014</td><td>3</td><td>DSP技术与实验(含理论)</td><td>1.5</td><td>正常</td><td>84</td><td>1.5</td>
		</tr><tr>
			<td>2014</td><td>3</td><td>数字图像处理课程设计</td><td>1</td><td>正常</td><td>86</td><td>1</td>
		</tr><tr>
			<td>2015</td><td>3</td><td>项目综合实践3</td><td>2</td><td>正常</td><td style="color:Red;">未评教</td><td>0</td>
		</tr><tr>
			<td>2012</td><td>3</td><td>大学英语1级听说</td><td>2</td><td>正常</td><td>78</td><td>2</td>
		</tr><tr>
			<td>2012</td><td>3</td><td>大学英语1级读写</td><td>2</td><td>正常</td><td>66</td><td>2</td>
		</tr><tr>
			<td>2013</td><td>1</td><td>大学英语2级听说</td><td>2</td><td>正常</td><td>69</td><td>2</td>
		</tr><tr>
			<td>2013</td><td>1</td><td>大学英语2级读写</td><td>2</td><td>正常</td><td>69</td><td>2</td>
		</tr><tr>
			<td>2013</td><td>3</td><td>大学英语3级听说</td><td>2</td><td>正常</td><td>41</td><td>0</td>
		</tr><tr>
			<td>2013</td><td>3</td><td>大学英语3级听说</td><td>2</td><td>补考</td><td>60</td><td>2</td>
		</tr><tr>
			<td>2013</td><td>3</td><td>大学英语3级读写</td><td>2</td><td>正常</td><td>69</td><td>2</td>
		</tr><tr>
			<td>2014</td><td>1</td><td>大学英语4级听说</td><td>2</td><td>正常</td><td>43</td><td>0</td>
		</tr><tr>
			<td>2014</td><td>1</td><td>大学英语4级听说</td><td>2</td><td>补考</td><td>60</td><td>2</td>
		</tr><tr>
			<td>2014</td><td>1</td><td>大学英语4级读写</td><td>2</td><td>正常</td><td>74</td><td>2</td>
		</tr><tr>
			<td>2013</td><td>1</td><td>就业指导课(一)</td><td>0.5</td><td>正常</td><td>及格</td><td>0.5</td>
		</tr><tr>
			<td>2015</td><td>1</td><td>就业指导课(二)</td><td>0.5</td><td>正常</td><td>中</td><td>0.5</td>
		</tr><tr>
			<td>2012</td><td>3</td><td>军事理论</td><td>0.5</td><td>正常</td><td>中</td><td>0.5</td>
		</tr><tr>
			<td>2012</td><td>3</td><td>军事训练</td><td>2.5</td><td>正常</td><td>良</td><td>2.5</td>
		</tr><tr>
			<td>2013</td><td>1</td><td>工程基础训练I</td><td>1</td><td>正常</td><td>93</td><td>1</td>
		</tr><tr>
			<td>2013</td><td>1</td><td>工程基础训练Ⅱ</td><td>1</td><td>正常</td><td>81</td><td>1</td>
		</tr><tr>
			<td>2012</td><td>3</td><td>马克思主义基本原理</td><td>3</td><td>正常</td><td>76</td><td>3</td>
		</tr><tr>
			<td>2014</td><td>1</td><td>中国近现代史纲要</td><td>2</td><td>正常</td><td>71</td><td>2</td>
		</tr><tr>
			<td>2013</td><td>3</td><td>毛泽东思想和中国特色社会主义理论体系概论</td><td>4</td><td>正常</td><td>84</td><td>4</td>
		</tr><tr>
			<td>2013</td><td>1</td><td>形势与政策(一)</td><td>0.5</td><td>正常</td><td>80</td><td>0.5</td>
		</tr><tr>
			<td>2014</td><td>1</td><td>形势与政策(二)</td><td>0.5</td><td>正常</td><td>90</td><td>0.5</td>
		</tr><tr>
			<td>2015</td><td>1</td><td>形势与政策(三)</td><td>0.5</td><td>正常</td><td>87</td><td>0.5</td>
		</tr><tr>
			<td>2013</td><td>1</td><td>思想道德修养与法律基础</td><td>3</td><td>正常</td><td>83</td><td>3</td>
		</tr><tr>
			<td>2013</td><td>3</td><td>中国近现代风云人物</td><td>1</td><td>正常</td><td>86</td><td>1</td>
		</tr>
	</table>
</div>
        <div>

</div>

            </div>
        </div>

<div>

	<input type="hidden" name="__EVENTTARGET" id="__EVENTTARGET" value="" />
	<input type="hidden" name="__EVENTARGUMENT" id="__EVENTARGUMENT" value="" />
	<input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="/wEWKgL/nf+3AQL5pJ/DDwKY5YbqAwLOyrSfCgKa/8n5CAKcv5WqDgLVtaKfCgKb2v2nDQKb2oHDAgKGzf/rAQKGzYOHCQKGzdfvCwKGzfuIAwKGzY+kCAKGzZPBAQKGzaf6BgKGzcuXDgKGzd+wBwKGzePtDALt9NH0CwLt9OWRAwLt9Mn4BQLt9N2VDQLt9OHOAgLt9PXrCwLt9JmHAwLt9K2gCALt9LHdAQLt9MX2BgKpl6yAAwKpl7C9CAKpl4SEDQKpl6ihAgLbxvmxDALExvmxDALFxvmxDALGxvmxDALHxvmxDAKTn4DADwKTn/TkBgLS+ZvbCQLM08eVCnUBhpB3hAJ4e1I7iuxe06V4pHG8" />
</div>
<script type="text/javascript">
<!--
var theForm = document.forms['aspnetForm'];
if (!theForm) {
    theForm = document.aspnetForm;
}
function __doPostBack(eventTarget, eventArgument) {
    if (!theForm.onsubmit || (theForm.onsubmit() != false)) {
        theForm.__EVENTTARGET.value = eventTarget;
        theForm.__EVENTARGUMENT.value = eventArgument;
        theForm.submit();
    }
}
// -->
</script>

</form>
</body>
</html>

"""

page = BeautifulSoup(htmldoc)
tr_title = page.find(attrs={'class':'HeaderStyle'})
text  = tr_title.find_next_siblings()
# print text

for tiaomu in text:
    if tiaomu.td.string == '2012':
        tiaomu2012 = []
        tiaomu2012.append(tiaomu)
        # print tiaomu2012
print tiaomu2012

# if tiaomu2012:
#     for foo in tiaomu2012:
#         for bar in foo:
#             print bar.string

# for i in range(10)
#     if i%2 == 0