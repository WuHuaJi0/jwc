#encoding:utf-8
from bs4 import BeautifulSoup
html_doc = """
<!doctype html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Document</title>
</head>
<body>

<form action="/xg/student/edit.do" method="post" id="f" name="f" enctype="multipart/form-data" class="am-form">
<!--图片旁边的div 是否结束-->
                  <h2><i class="am-icon-cogs"></i>&nbsp;基本信息</h2>
           <div class="am-g">
               <div class="am-u-sm-8">
                   <ul class="am-avg-sm-1 am-avg-md-1 am-avg-lg-2 am-thumbnails am-margin-right">
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">姓名：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
                            <input type="text" name="STD_INFO_XM"  readonly value="施云飞"/>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">学号：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
                            <input type="text" name="STD_INFO_XH"  readonly value="2012136107"/>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">曾用名：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
            <input type="text"  name="STD_INFO_CYM" class='js-pattern-'''     value=""/>

                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">性别：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
                            <input type="text" name="STD_INFO_XB"  readonly value="男"/>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">出生日期：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
                            <input type="text" name="STD_INFO_CSRQ"  readonly value="19930303"/>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">民族：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
                            <input type="text" name="STD_INFO_MZ"  readonly value="汉族"/>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">证件类型：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
<div class="am-input-icon"><input type="text" id="STD_INFO_ZJLX_iiiiid_" name="STD_INFO_ZJLX" placeholder="请选择" onclick="select_STD_INFO_ZJLX_iiiiid_()" style="" value="身份证"  required /><i style="cursor:pointer;" class="am-icon-search" onclick="select_STD_INFO_ZJLX_iiiiid_()"></i></div><script type="text/javascript">
    function call_STD_INFO_ZJLX_iiiiid_(params){
        if(params!=null&&params!="") {
            var selectValues = params.split(",");
            var value = "";
            var hiddenValue = "";
            for (var i = 0; i < selectValues.length; i++) {
                var item = selectValues[i].split("|||");
                if (i > 0) {
                    value += ",";
                    hiddenValue += ",";
                }
                hiddenValue += item[0];
                value += item[1];
            }

            $("#STD_INFO_ZJLX_iiiiid_").val(value);
        }
        else{

            $("#STD_INFO_ZJLX_iiiiid_").val("");
        }
                $("#STD_INFO_ZJLX_iiiiid_").focus();
    }
    function select_STD_INFO_ZJLX_iiiiid_(){
        var hidden = "";

            var hiddenValue = encodeURI(encodeURI($("#STD_INFO_ZJLX_iiiiid_").val()));
        $.dialog("/xg/public/common.do?multiple=&parentId=91117&hidden="+hidden+"&type=code&value="+hiddenValue+"&callback=call_STD_INFO_ZJLX_iiiiid_","请选择","700px","400px");
    }
</script>
     <span class="text-red">*</span>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">证件号码：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
                            <input type="text" name="STD_INFO_SFZH"  readonly value="420881199303032976"/>
                                    </div>

            </div>
        </li>
        </div>
        <div class="am-u-sm-4">
            <ul class="am-avg-sm-1 am-avg-md-1 am-avg-lg-1 am-thumbnails am-margin-right">
    <div class="am-form-group am-g">
        <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">照片：</label></div>
        <div class="am-u-sm-7 clear_m_p  am-input-group">
                <img style="width:120px;height:160px;" src="/xg/vfs/vfs.do?path=2015/STD_INFO/RXZP/2012136107.jpg"/>
                <!-- 学生修改-->
                    <input type="file"  name="STD_INFO_RXZP" onchange="handleFiles(this.files)" style="width:200px;"/>
                        </div>
    </div>
            </ul>
        </div>
        </div>
       <ul class="am-avg-sm-1 am-avg-md-2 am-avg-lg-3 am-thumbnails am-margin-right">
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">学院：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
                            <input type="text" name="STD_INFO_XY"  readonly value="计算机与信息学院"/>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">专业：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
                            <input type="text" name="STD_INFO_ZY"  readonly value="通信工程"/>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">班级：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
                            <input type="text" name="STD_INFO_BJMC"  readonly value="20121361"/>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">入学年月：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
                            <input type="text" name="STD_INFO_RXNY"  readonly value="2012"/>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">政治面貌：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
                            <input type="text" name="STD_INFO_ZZMM"  readonly value="共青团员"/>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">考生号：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
                            <input type="text" name="STD_INFO_BKH"  readonly value="12420881153373"/>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">考生学生类别：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
<div class="am-input-icon"><input type="text" id="STD_INFO_KSXSLB_iiiiid_" name="STD_INFO_KSXSLB" placeholder="请选择" onclick="select_STD_INFO_KSXSLB_iiiiid_()" style="" value="理科"/><i style="cursor:pointer;" class="am-icon-search" onclick="select_STD_INFO_KSXSLB_iiiiid_()"></i></div><script type="text/javascript">
    function call_STD_INFO_KSXSLB_iiiiid_(params){
        if(params!=null&&params!="") {
            var selectValues = params.split(",");
            var value = "";
            var hiddenValue = "";
            for (var i = 0; i < selectValues.length; i++) {
                var item = selectValues[i].split("|||");
                if (i > 0) {
                    value += ",";
                    hiddenValue += ",";
                }
                hiddenValue += item[0];
                value += item[1];
            }

            $("#STD_INFO_KSXSLB_iiiiid_").val(value);
        }
        else{

            $("#STD_INFO_KSXSLB_iiiiid_").val("");
        }
                $("#STD_INFO_KSXSLB_iiiiid_").focus();
    }
    function select_STD_INFO_KSXSLB_iiiiid_(){
        var hidden = "";

            var hiddenValue = encodeURI(encodeURI($("#STD_INFO_KSXSLB_iiiiid_").val()));
        $.dialog("/xg/public/common.do?multiple=&parentId=30011&hidden="+hidden+"&type=code&value="+hiddenValue+"&callback=call_STD_INFO_KSXSLB_iiiiid_","请选择","700px","400px");
    }
</script>

                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">工龄军龄（年）：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
            <input type="text"  name="STD_INFO_GLJL" class='js-pattern-number'     value=""/>

                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">起始站：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
                            <input type="text" name="STD_INFO_CCQSZ"  readonly value=""/>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">终止站：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
            <input type="text"  name="STD_INFO_CCZDZ" class='js-pattern-'''  placeholder="请输入火车票上站点名，如“汉口”"   required   value="钟祥"/>
     <span class="text-red">*</span>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">是否孤儿：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
<select id="STD_INFO_SFGE_iiiiid_" name="STD_INFO_SFGE"  data-am-selected>
        <option value="" ></option>
        <option value="是" >是</option>
        <option value="否" selected>否</option>
</select>
     <span class="text-red">*</span>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">是否残疾：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
<select id="STD_INFO_SFCJ_iiiiid_" name="STD_INFO_SFCJ"  data-am-selected>
        <option value="" ></option>
        <option value="是" >是</option>
        <option value="否" selected>否</option>
</select>
     <span class="text-red">*</span>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">学籍状态：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
                            <input type="text" name="STD_INFO_XJZT"  readonly value="在籍"/>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">在校状态：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
                            <input type="text" name="STD_INFO_ZXZT"  readonly value="是"/>
                                    </div>

            </div>
        </li>
       </ul>
           <h2><i class="am-icon-cogs"></i>&nbsp;其他信息</h2>
           <ul class="am-avg-sm-1 am-avg-md-2 am-avg-lg-3 am-thumbnails am-margin-right"><!-- 没有图片时 每行显示3个 -->
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">籍贯：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
<div class="am-input-icon"><input type="text" id="STD_INFO_JG_iiiiid_" name="STD_INFO_JG" placeholder="请选择" onclick="select_STD_INFO_JG_iiiiid_()" value="湖北省钟祥市"  required /><i style="cursor:pointer;" class="am-icon-search" onclick="select_STD_INFO_JG_iiiiid_()"></i></div>    <script type="text/javascript">
        function call_STD_INFO_JG_iiiiid_(params){
            if(params!=null&&params!="") {
                var provice = params.provice;
                var city = params.city;
                var locale = '';
                if ( params.locale ){
                    locale = params.locale;
                }
                $("#STD_INFO_JG_iiiiid_").val(provice+city+locale);
            }
            else{
                $("#STD_INFO_JG_iiiiid_").val("");
            }
            $("#STD_INFO_JG_iiiiid_").focus();
        }
        function select_STD_INFO_JG_iiiiid_(){
            $.dialog("/xg/public/area.do?callback=call_STD_INFO_JG_iiiiid_","请选择","700px","400px");
        }
    </script>
     <span class="text-red">*</span>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">出生地：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
<div class="am-input-icon"><input type="text" id="STD_INFO_CSD_iiiiid_" name="STD_INFO_CSD" placeholder="请选择" onclick="select_STD_INFO_CSD_iiiiid_()" value="湖北钟祥市"  required /><i style="cursor:pointer;" class="am-icon-search" onclick="select_STD_INFO_CSD_iiiiid_()"></i></div>    <script type="text/javascript">
        function call_STD_INFO_CSD_iiiiid_(params){
            if(params!=null&&params!="") {
                var provice = params.provice;
                var city = params.city;
                var locale = '';
                if ( params.locale ){
                    locale = params.locale;
                }
                $("#STD_INFO_CSD_iiiiid_").val(provice+city+locale);
            }
            else{
                $("#STD_INFO_CSD_iiiiid_").val("");
            }
            $("#STD_INFO_CSD_iiiiid_").focus();
        }
        function select_STD_INFO_CSD_iiiiid_(){
            $.dialog("/xg/public/area.do?callback=call_STD_INFO_CSD_iiiiid_","请选择","700px","400px");
        }
    </script>
     <span class="text-red">*</span>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">身高（cm）：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
            <input type="text"  name="STD_INFO_SG" class='js-pattern-number'  placeholder="请输入数字，如“180”"   required   value="168"/>
     <span class="text-red">*</span>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">体重（kg）：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
            <input type="text"  name="STD_INFO_TZ" class='js-pattern-number'  placeholder="请输入数字，如“60”"   required   value="62"/>
     <span class="text-red">*</span>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">家庭住址：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
            <input type="text"  name="STD_INFO_JTZZ" class='js-pattern-'''  placeholder="请输入户口所在地的家庭住址"   required   value="湖北省荆门市钟祥市磷矿镇刘冲花冲生活区"/>
     <span class="text-red">*</span>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">家庭现住址：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
            <input type="text"  name="STD_INFO_XZZ" class='js-pattern-'''  placeholder="请输入父母常年居住地址"    value="湖北省钟祥市磷矿镇老教育组"/>

                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">家庭住址邮编：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
            <input type="text"  name="STD_INFO_JTZZYB" class='js-pattern-'''    required   value="431915"/>
     <span class="text-red">*</span>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">家庭电话：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
            <input type="text"  name="STD_INFO_JTDH" class='js-pattern-'''    required   value="13634017578"/>
     <span class="text-red">*</span>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">毕业中学：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
            <input type="text"  name="STD_INFO_BYZX" class='js-pattern-'''    required   value="钟祥六中"/>
     <span class="text-red">*</span>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">毕业中学邮编 ：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
            <input type="text"  name="STD_INFO_BYXXYB" class='js-pattern-'''    required   value="431900"/>
     <span class="text-red">*</span>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">本人手机：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
            <input type="text"  name="STD_INFO_SJ" class='js-pattern-tel'    required   value="15549332883"/>
     <span class="text-red">*</span>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">本人手机2：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
            <input type="text"  name="STD_INFO_XNDH" class='js-pattern-number'     value="07176290780"/>

                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">校内地址：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
            <input type="text"  name="STD_INFO_XNDZ" class='js-pattern-'''  placeholder="如“校本部西苑01#楼第1层103”"   required   value="校本部欣苑02#楼第6层624"/>
     <span class="text-red">*</span>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">紧急联系人：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
            <input type="text"  name="STD_INFO_ZYDZ" class='js-pattern-'''  placeholder="如寝室长、班长、班主任姓名等"   required   value="夏坤"/>
     <span class="text-red">*</span>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">紧急联系电话：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
            <input type="text"  name="STD_INFO_LXDH" class='js-pattern-number'    required   value="15629338260"/>
     <span class="text-red">*</span>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">QQ号：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
            <input type="text"  name="STD_INFO_QQH" class='js-pattern-QQ'    required   value="80672451"/>
     <span class="text-red">*</span>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">电子邮件：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
            <input type="text"  name="STD_INFO_EMAIL" class='js-pattern-email'    required   value="80672451@qq.com"/>
     <span class="text-red">*</span>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">微信号：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
            <input type="text"  name="STD_INFO_MSN" class='js-pattern-'''     value=""/>

                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">本人通讯地址：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
            <input type="text"  name="STD_INFO_TXDZ" class='js-pattern-'''  placeholder="如“×省×市三峡大学×学院×班”"   required   value="宜昌市三峡大学计算机与信息学院通信工程系20121361班"/>
     <span class="text-red">*</span>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">学校邮政编码：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
                            <input type="text" name="STD_INFO_YZBM"  readonly value=""/>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">入党时间：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
                            <input type="text" name="STD_INFO_RDSJ"  readonly value=""/>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">发展时间：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
                            <input type="text" name="STD_INFO_FZSJ"  readonly value=""/>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">转正时间：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
                            <input type="text" name="STD_INFO_ZZSJ"  readonly value=""/>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">入党积极分子时间：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
                            <input type="text" name="STD_INFO_RDJJFZSJ"  readonly value=""/>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">党校结业时间：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
                            <input type="text" name="STD_INFO_DXJYSJ"  readonly value=""/>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">农行卡号：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
            <input type="text"  name="STD_INFO_JLKKH" class='js-pattern-yhk'    required   value="6228210770015681617"/>
     <span class="text-red">*</span>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">校园卡号：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
                            <input type="text" name="STD_INFO_XSYKT"  readonly value=""/>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">所在校区：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
<div class="am-input-icon"><input type="text" id="STD_INFO_XQ_iiiiid_" name="STD_INFO_XQ" placeholder="请选择" onclick="select_STD_INFO_XQ_iiiiid_()" style="" value="校本部"  required /><i style="cursor:pointer;" class="am-icon-search" onclick="select_STD_INFO_XQ_iiiiid_()"></i></div><script type="text/javascript">
    function call_STD_INFO_XQ_iiiiid_(params){
        if(params!=null&&params!="") {
            var selectValues = params.split(",");
            var value = "";
            var hiddenValue = "";
            for (var i = 0; i < selectValues.length; i++) {
                var item = selectValues[i].split("|||");
                if (i > 0) {
                    value += ",";
                    hiddenValue += ",";
                }
                hiddenValue += item[0];
                value += item[1];
            }

            $("#STD_INFO_XQ_iiiiid_").val(value);
        }
        else{

            $("#STD_INFO_XQ_iiiiid_").val("");
        }
                $("#STD_INFO_XQ_iiiiid_").focus();
    }
    function select_STD_INFO_XQ_iiiiid_(){
        var hidden = "";

            var hiddenValue = encodeURI(encodeURI($("#STD_INFO_XQ_iiiiid_").val()));
        $.dialog("/xg/public/common.do?multiple=&parentId=30010&hidden="+hidden+"&type=code&value="+hiddenValue+"&callback=call_STD_INFO_XQ_iiiiid_","请选择","700px","400px");
    }
</script>
     <span class="text-red">*</span>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">特长：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
            <input type="text"  name="STD_INFO_TC" class='js-pattern-'''     value="阅读，打篮球。"/>

                                    </div>

            </div>
        </li>
       </ul>
           <h2><i class="am-icon-cogs"></i>&nbsp;奖惩信息</h2>
           <ul class="am-avg-sm-1 am-avg-md-2 am-avg-lg-3 am-thumbnails am-margin-right"><!-- 没有图片时 每行显示3个 -->
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">入校前获得何种奖励：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
            <input type="text"  name="STD_INFO_GZJLQK" class='js-pattern-'''     value="湖北省物理竞赛省二等奖"/>

                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">入校前受过何种处分：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
            <input type="text"  name="STD_INFO_GZCFQK" class='js-pattern-'''     value="无"/>

                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">担任何种职务：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
            <input type="text"  name="STD_INFO_GZZW" class='js-pattern-'''     value="课代表  班长"/>

                                    </div>

            </div>
        </li>
       </ul>
           <h2><i class="am-icon-cogs"></i>&nbsp;家庭经济状况</h2>
           <ul class="am-avg-sm-1 am-avg-md-2 am-avg-lg-3 am-thumbnails am-margin-right"><!-- 没有图片时 每行显示3个 -->
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">是否独生子女：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
<select id="STD_INFO_SFDSZN_iiiiid_" name="STD_INFO_SFDSZN"  data-am-selected>
        <option value="" ></option>
        <option value="是" selected>是</option>
        <option value="否" >否</option>
</select>
     <span class="text-red">*</span>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">是否烈士子女：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
<select id="STD_INFO_SFLSZN_iiiiid_" name="STD_INFO_SFLSZN"  data-am-selected>
        <option value="" ></option>
        <option value="是" >是</option>
        <option value="否" selected>否</option>
</select>
     <span class="text-red">*</span>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">兄弟姐妹数：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
            <input type="text"  name="STD_INFO_XDJMS" class='js-pattern-number'    required   value="0"/>
     <span class="text-red">*</span>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">家庭人口数：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
            <input type="text"  name="STD_INFO_JTRKS" class='js-pattern-number'    required   value="3"/>
     <span class="text-red">*</span>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">全年收入总数（元）：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
            <input type="text"  name="STD_INFO_QNSRZS" class='js-pattern-'''    required   value="50000"/>
     <span class="text-red">*</span>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">是否低保家庭：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
<select id="STD_INFO_SFPKJT_iiiiid_" name="STD_INFO_SFPKJT"  data-am-selected>
        <option value="" ></option>
        <option value="是" selected>是</option>
        <option value="否" >否</option>
</select>
     <span class="text-red">*</span>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">是否享受低保：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
<select id="STD_INFO_SFSGZZ_iiiiid_" name="STD_INFO_SFSGZZ"  data-am-selected>
        <option value="" ></option>
        <option value="是" selected>是</option>
        <option value="否" >否</option>
</select>
     <span class="text-red">*</span>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">受资助项目：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
            <input type="text"  name="STD_INFO_SZZXM" class='js-pattern-'''     value="低保"/>

                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">受资助总额（元）：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
            <input type="text"  name="STD_INFO_SZZZE" class='js-pattern-number'     value="2000"/>

                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">是否单亲家庭：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
<select id="STD_INFO_SFDQJT_iiiiid_" name="STD_INFO_SFDQJT"  data-am-selected>
        <option value="" ></option>
        <option value="是" >是</option>
        <option value="否" selected>否</option>
</select>
     <span class="text-red">*</span>
                                    </div>

            </div>
        </li>
       </ul>
           <h2><i class="am-icon-cogs"></i>&nbsp;个人信息</h2>
           <ul class="am-avg-sm-1 am-avg-md-2 am-avg-lg-3 am-thumbnails am-margin-right"><!-- 没有图片时 每行显示3个 -->
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">学生类别：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
                            <input type="text" name="STD_INFO_XSLB"  readonly value="校本部"/>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">培养层次：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
                            <input type="text" name="STD_INFO_PYCC"  readonly value="本科"/>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">血型：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
<div class="am-input-icon"><input type="text" id="STD_INFO_XX_iiiiid_" name="STD_INFO_XX" placeholder="请选择" onclick="select_STD_INFO_XX_iiiiid_()" style="" value="O型"/><i style="cursor:pointer;" class="am-icon-search" onclick="select_STD_INFO_XX_iiiiid_()"></i></div><script type="text/javascript">
    function call_STD_INFO_XX_iiiiid_(params){
        if(params!=null&&params!="") {
            var selectValues = params.split(",");
            var value = "";
            var hiddenValue = "";
            for (var i = 0; i < selectValues.length; i++) {
                var item = selectValues[i].split("|||");
                if (i > 0) {
                    value += ",";
                    hiddenValue += ",";
                }
                hiddenValue += item[0];
                value += item[1];
            }

            $("#STD_INFO_XX_iiiiid_").val(value);
        }
        else{

            $("#STD_INFO_XX_iiiiid_").val("");
        }
                $("#STD_INFO_XX_iiiiid_").focus();
    }
    function select_STD_INFO_XX_iiiiid_(){
        var hidden = "";

            var hiddenValue = encodeURI(encodeURI($("#STD_INFO_XX_iiiiid_").val()));
        $.dialog("/xg/public/common.do?multiple=&parentId=20017&hidden="+hidden+"&type=code&value="+hiddenValue+"&callback=call_STD_INFO_XX_iiiiid_","请选择","700px","400px");
    }
</script>

                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">婚姻状况：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
<div class="am-input-icon"><input type="text" id="STD_INFO_HYZK_iiiiid_" name="STD_INFO_HYZK" placeholder="请选择" onclick="select_STD_INFO_HYZK_iiiiid_()" style="" value="未婚"/><i style="cursor:pointer;" class="am-icon-search" onclick="select_STD_INFO_HYZK_iiiiid_()"></i></div><script type="text/javascript">
    function call_STD_INFO_HYZK_iiiiid_(params){
        if(params!=null&&params!="") {
            var selectValues = params.split(",");
            var value = "";
            var hiddenValue = "";
            for (var i = 0; i < selectValues.length; i++) {
                var item = selectValues[i].split("|||");
                if (i > 0) {
                    value += ",";
                    hiddenValue += ",";
                }
                hiddenValue += item[0];
                value += item[1];
            }

            $("#STD_INFO_HYZK_iiiiid_").val(value);
        }
        else{

            $("#STD_INFO_HYZK_iiiiid_").val("");
        }
                $("#STD_INFO_HYZK_iiiiid_").focus();
    }
    function select_STD_INFO_HYZK_iiiiid_(){
        var hidden = "";

            var hiddenValue = encodeURI(encodeURI($("#STD_INFO_HYZK_iiiiid_").val()));
        $.dialog("/xg/public/common.do?multiple=&parentId=20003&hidden="+hidden+"&type=code&value="+hiddenValue+"&callback=call_STD_INFO_HYZK_iiiiid_","请选择","700px","400px");
    }
</script>

                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">生源地区：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
                            <input type="text" name="STD_INFO_LYDQ"  readonly value="湖北省钟祥市"/>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">户口所在地：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
            <input type="text"  name="STD_INFO_HKD" class='js-pattern-'''  placeholder="身份证签发机关名，“××派出所”"   required   value="湖北省钟祥市公安局"/>
     <span class="text-red">*</span>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">户口详细地址：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
            <input type="text"  name="STD_INFO_HKSZDZ" class='js-pattern-'''  placeholder="身份证正面的住址信息"   required   value="湖北省钟祥市磷矿镇刘冲花冲生活区42号"/>
     <span class="text-red">*</span>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">户口性质：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
<div class="am-input-icon"><input type="text" id="STD_INFO_HKXZ_iiiiid_" name="STD_INFO_HKXZ" placeholder="请选择" onclick="select_STD_INFO_HKXZ_iiiiid_()" style="" value="非农业户口"  required /><i style="cursor:pointer;" class="am-icon-search" onclick="select_STD_INFO_HKXZ_iiiiid_()"></i></div><script type="text/javascript">
    function call_STD_INFO_HKXZ_iiiiid_(params){
        if(params!=null&&params!="") {
            var selectValues = params.split(",");
            var value = "";
            var hiddenValue = "";
            for (var i = 0; i < selectValues.length; i++) {
                var item = selectValues[i].split("|||");
                if (i > 0) {
                    value += ",";
                    hiddenValue += ",";
                }
                hiddenValue += item[0];
                value += item[1];
            }

            $("#STD_INFO_HKXZ_iiiiid_").val(value);
        }
        else{

            $("#STD_INFO_HKXZ_iiiiid_").val("");
        }
                $("#STD_INFO_HKXZ_iiiiid_").focus();
    }
    function select_STD_INFO_HKXZ_iiiiid_(){
        var hidden = "";

            var hiddenValue = encodeURI(encodeURI($("#STD_INFO_HKXZ_iiiiid_").val()));
        $.dialog("/xg/public/common.do?multiple=&parentId=20005&hidden="+hidden+"&type=code&value="+hiddenValue+"&callback=call_STD_INFO_HKXZ_iiiiid_","请选择","700px","400px");
    }
</script>
     <span class="text-red">*</span>
                                    </div>

            </div>
        </li>
        <li>
            <div class="am-form-group am-g">
                <div class="am-u-sm-5" style="text-align: right;"><label class="label-normal">综合备注：</label></div>
                <div class="am-u-sm-7 clear_m_p am-input-group">
                    <!-- 学生修改-->
            <input type="text"  name="STD_INFO_ZHBZ" class='js-pattern-'''     value=""/>

                                    </div>

            </div>
        </li>
        </ul>
<script type="text/javascript">
var add_index_js=200;
function  addLi(tableid) {
    var lihtml = $("#am-li-" + tableid).html();
    lihtml = lihtml.replace(/iiiiid/g,add_index_js + "");
    $("#am-ul-" + tableid).append("<li>" + lihtml + "</li>");
    add_index_js = add_index_js + 1;
}
$(document).ready(function(){
    $('#f').validator({});
});

function handleFiles(f){
    var result = "";
    for (var i = 0; i < f.length; i++) {
        var type = f[i].name.substr(f[i].name.lastIndexOf(".")).toLowerCase();
        if(f[i].size > 102400){
            $.alert("请上传小于100K的照片！");
        }else if( '.gif' != type && '.jpg' != type && '.png' != type && '.jpeg' != type){
            $.alert("请固定格式的照片(gif、jpg、png、jpeg)！");
        }
    }
}
</script>
    <div id="hidden_div">
    </div>
</form>
</body>
</html>
"""

soup = BeautifulSoup(html_doc)
divSum = soup.find_all('div','am-form-group am-g')

nameDiv = divSum[0].find_all('div')
name = nameDiv[1].input['value']

numDiv = divSum[1].find_all('div')
num = numDiv[1].input['value']


print name,num
# print name,num


# for divlist in divSum:
#     list = divlist.find_all('div')
#     # print len(list)
#     try:
#         key =  list[0].label.string
#         value =  list[1].input['value']
#         print key,value
#     except:
#         pass
            # print divlist.label.string
            # print divlist.input['value']
        # divlist = divSum[0].find_all('div')
        # print divlist[0].label.string
        # print divlist[1].input['value']