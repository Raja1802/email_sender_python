#!/usr/bin/env python
# coding: utf-8

# In[18]:


# # Python code to illustrate Sending mail 
# # to multiple users 
# # from your Gmail account 
# import smtplib 

# # list of email_id to send the mail 
# li = ["ajar.shopinsta@gmail.com"] 

# for dest in li: 
# 	s = smtplib.SMTP('smtp.gmail.com', 587) 
# 	s.starttls() 
# 	s.login("ajar.mailer.com@gmail.com", "Raja@1802") 
# 	message = "hellow world"
# 	s.sendmail("ajar.mailer.com@gmail.com", dest, message) 
# 	s.quit() 
# import pandas as pd
# import numpy as np
# data = pd.read_csv("0.csv")
# data.head()
# data.shape
# data["emails"].head()
# inde = 0
# for email in data["emails"]:
#     print(email)
#     print(inde)
#     inde = inde + 1


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[17]:


import smtplib
import email.message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# server = smtplib.SMTP('smtp.gmail.com:587')
 
html = u"""
<!doctype html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
    <head>
        <!-- NAME: SELL PRODUCTS -->
        <!--[if gte mso 15]>
        <xml>
            <o:OfficeDocumentSettings>
            <o:AllowPNG/>
            <o:PixelsPerInch>96</o:PixelsPerInch>
            </o:OfficeDocumentSettings>
        </xml>
        <![endif]-->
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Your Christmas Shopping deals</title>
        
    <style type="text/css">
		p{
			margin:10px 0;
			padding:0;
		}
		table{
			border-collapse:collapse;
		}
		h1,h2,h3,h4,h5,h6{
			display:block;
			margin:0;
			padding:0;
		}
		img,a img{
			border:0;
			height:auto;
			outline:none;
			text-decoration:none;
		}
		body,#bodyTable,#bodyCell{
			height:100%;
			margin:0;
			padding:0;
			width:100%;
		}
		.mcnPreviewText{
			display:none !important;
		}
		#outlook a{
			padding:0;
		}
		img{
			-ms-interpolation-mode:bicubic;
		}
		table{
			mso-table-lspace:0pt;
			mso-table-rspace:0pt;
		}
		.ReadMsgBody{
			width:100%;
		}
		.ExternalClass{
			width:100%;
		}
		p,a,li,td,blockquote{
			mso-line-height-rule:exactly;
		}
		a[href^=tel],a[href^=sms]{
			color:inherit;
			cursor:default;
			text-decoration:none;
		}
		p,a,li,td,body,table,blockquote{
			-ms-text-size-adjust:100%;
			-webkit-text-size-adjust:100%;
		}
		.ExternalClass,.ExternalClass p,.ExternalClass td,.ExternalClass div,.ExternalClass span,.ExternalClass font{
			line-height:100%;
		}
		a[x-apple-data-detectors]{
			color:inherit !important;
			text-decoration:none !important;
			font-size:inherit !important;
			font-family:inherit !important;
			font-weight:inherit !important;
			line-height:inherit !important;
		}
		.templateContainer{
			max-width:600px !important;
		}
		a.mcnButton{
			display:block;
		}
		.mcnImage,.mcnRetinaImage{
			vertical-align:bottom;
		}
		.mcnTextContent{
			word-break:break-word;
		}
		.mcnTextContent img{
			height:auto !important;
		}
		.mcnDividerBlock{
			table-layout:fixed !important;
		}
	/*
	@tab Page
	@section Heading 1
	@style heading 1
	*/
		h1{
			/*@editable*/color:#222222;
			/*@editable*/font-family:Helvetica;
			/*@editable*/font-size:40px;
			/*@editable*/font-style:normal;
			/*@editable*/font-weight:bold;
			/*@editable*/line-height:150%;
			/*@editable*/letter-spacing:normal;
			/*@editable*/text-align:center;
		}
	/*
	@tab Page
	@section Heading 2
	@style heading 2
	*/
		h2{
			/*@editable*/color:#222222;
			/*@editable*/font-family:Helvetica;
			/*@editable*/font-size:34px;
			/*@editable*/font-style:normal;
			/*@editable*/font-weight:bold;
			/*@editable*/line-height:150%;
			/*@editable*/letter-spacing:normal;
			/*@editable*/text-align:left;
		}
	/*
	@tab Page
	@section Heading 3
	@style heading 3
	*/
		h3{
			/*@editable*/color:#444444;
			/*@editable*/font-family:Helvetica;
			/*@editable*/font-size:22px;
			/*@editable*/font-style:normal;
			/*@editable*/font-weight:bold;
			/*@editable*/line-height:150%;
			/*@editable*/letter-spacing:normal;
			/*@editable*/text-align:left;
		}
	/*
	@tab Page
	@section Heading 4
	@style heading 4
	*/
		h4{
			/*@editable*/color:#949494;
			/*@editable*/font-family:Georgia;
			/*@editable*/font-size:20px;
			/*@editable*/font-style:italic;
			/*@editable*/font-weight:normal;
			/*@editable*/line-height:125%;
			/*@editable*/letter-spacing:normal;
			/*@editable*/text-align:left;
		}
	/*
	@tab Header
	@section Header Container Style
	*/
		#templateHeader{
			/*@editable*/background-color:#ffffff;
			/*@editable*/background-image:url("https://mcusercontent.com/0696b552530703b1e1a9285fa/images/44e7d80a-8545-43bd-b334-a9176bc273b4.jpg");
			/*@editable*/background-repeat:no-repeat;
			/*@editable*/background-position:center;
			/*@editable*/background-size:cover;
			/*@editable*/border-top:0;
			/*@editable*/border-bottom:0;
			/*@editable*/padding-top:62px;
			/*@editable*/padding-bottom:62px;
		}
	/*
	@tab Header
	@section Header Interior Style
	*/
		.headerContainer{
			/*@editable*/background-color:transparent;
			/*@editable*/background-image:none;
			/*@editable*/background-repeat:no-repeat;
			/*@editable*/background-position:center;
			/*@editable*/background-size:cover;
			/*@editable*/border-top:0;
			/*@editable*/border-bottom:0;
			/*@editable*/padding-top:0;
			/*@editable*/padding-bottom:0;
		}
	/*
	@tab Header
	@section Header Text
	*/
		.headerContainer .mcnTextContent,.headerContainer .mcnTextContent p{
			/*@editable*/color:#757575;
			/*@editable*/font-family:Helvetica;
			/*@editable*/font-size:16px;
			/*@editable*/line-height:150%;
			/*@editable*/text-align:left;
		}
	/*
	@tab Header
	@section Header Link
	*/
		.headerContainer .mcnTextContent a,.headerContainer .mcnTextContent p a{
			/*@editable*/color:#007C89;
			/*@editable*/font-weight:normal;
			/*@editable*/text-decoration:underline;
		}
	/*
	@tab Body
	@section Body Container Style
	*/
		#templateBody{
			/*@editable*/background-color:#ffffff;
			/*@editable*/background-image:none;
			/*@editable*/background-repeat:no-repeat;
			/*@editable*/background-position:50% 50%;
			/*@editable*/background-size:cover;
			/*@editable*/border-top:0;
			/*@editable*/border-bottom:0;
			/*@editable*/padding-top:99px;
			/*@editable*/padding-bottom:99px;
		}
	/*
	@tab Body
	@section Body Interior Style
	*/
		.bodyContainer{
			/*@editable*/background-color:transparent;
			/*@editable*/background-image:none;
			/*@editable*/background-repeat:no-repeat;
			/*@editable*/background-position:center;
			/*@editable*/background-size:cover;
			/*@editable*/border-top:0;
			/*@editable*/border-bottom:0;
			/*@editable*/padding-top:0;
			/*@editable*/padding-bottom:0;
		}
	/*
	@tab Body
	@section Body Text
	*/
		.bodyContainer .mcnTextContent,.bodyContainer .mcnTextContent p{
			/*@editable*/color:#757575;
			/*@editable*/font-family:Helvetica;
			/*@editable*/font-size:16px;
			/*@editable*/line-height:150%;
			/*@editable*/text-align:left;
		}
	/*
	@tab Body
	@section Body Link
	*/
		.bodyContainer .mcnTextContent a,.bodyContainer .mcnTextContent p a{
			/*@editable*/color:#007C89;
			/*@editable*/font-weight:normal;
			/*@editable*/text-decoration:underline;
		}
	/*
	@tab Footer
	@section Footer Style
	*/
		#templateFooter{
			/*@editable*/background-color:#222222;
			/*@editable*/background-image:none;
			/*@editable*/background-repeat:no-repeat;
			/*@editable*/background-position:center;
			/*@editable*/background-size:cover;
			/*@editable*/border-top:0;
			/*@editable*/border-bottom:0;
			/*@editable*/padding-top:0px;
			/*@editable*/padding-bottom:0px;
		}
	/*
	@tab Footer
	@section Footer Interior Style
	*/
		.footerContainer{
			/*@editable*/background-color:transparent;
			/*@editable*/background-image:none;
			/*@editable*/background-repeat:no-repeat;
			/*@editable*/background-position:center;
			/*@editable*/background-size:cover;
			/*@editable*/border-top:0;
			/*@editable*/border-bottom:0;
			/*@editable*/padding-top:0;
			/*@editable*/padding-bottom:0;
		}
	/*
	@tab Footer
	@section Footer Text
	*/
		.footerContainer .mcnTextContent,.footerContainer .mcnTextContent p{
			/*@editable*/color:#FFFFFF;
			/*@editable*/font-family:Helvetica;
			/*@editable*/font-size:12px;
			/*@editable*/line-height:150%;
			/*@editable*/text-align:center;
		}
	/*
	@tab Footer
	@section Footer Link
	*/
		.footerContainer .mcnTextContent a,.footerContainer .mcnTextContent p a{
			/*@editable*/color:#FFFFFF;
			/*@editable*/font-weight:normal;
			/*@editable*/text-decoration:underline;
		}
	@media only screen and (min-width:768px){
		.templateContainer{
			width:600px !important;
		}

}	@media only screen and (max-width: 480px){
		body,table,td,p,a,li,blockquote{
			-webkit-text-size-adjust:none !important;
		}

}	@media only screen and (max-width: 480px){
		body{
			width:100% !important;
			min-width:100% !important;
		}

}	@media only screen and (max-width: 480px){
		.mcnRetinaImage{
			max-width:100% !important;
		}

}	@media only screen and (max-width: 480px){
		.mcnImage{
			width:100% !important;
		}

}	@media only screen and (max-width: 480px){
		.mcnCartContainer,.mcnCaptionTopContent,.mcnRecContentContainer,.mcnCaptionBottomContent,.mcnTextContentContainer,.mcnBoxedTextContentContainer,.mcnImageGroupContentContainer,.mcnCaptionLeftTextContentContainer,.mcnCaptionRightTextContentContainer,.mcnCaptionLeftImageContentContainer,.mcnCaptionRightImageContentContainer,.mcnImageCardLeftTextContentContainer,.mcnImageCardRightTextContentContainer,.mcnImageCardLeftImageContentContainer,.mcnImageCardRightImageContentContainer{
			max-width:100% !important;
			width:100% !important;
		}

}	@media only screen and (max-width: 480px){
		.mcnBoxedTextContentContainer{
			min-width:100% !important;
		}

}	@media only screen and (max-width: 480px){
		.mcnImageGroupContent{
			padding:9px !important;
		}

}	@media only screen and (max-width: 480px){
		.mcnCaptionLeftContentOuter .mcnTextContent,.mcnCaptionRightContentOuter .mcnTextContent{
			padding-top:9px !important;
		}

}	@media only screen and (max-width: 480px){
		.mcnImageCardTopImageContent,.mcnCaptionBottomContent:last-child .mcnCaptionBottomImageContent,.mcnCaptionBlockInner .mcnCaptionTopContent:last-child .mcnTextContent{
			padding-top:18px !important;
		}

}	@media only screen and (max-width: 480px){
		.mcnImageCardBottomImageContent{
			padding-bottom:9px !important;
		}

}	@media only screen and (max-width: 480px){
		.mcnImageGroupBlockInner{
			padding-top:0 !important;
			padding-bottom:0 !important;
		}

}	@media only screen and (max-width: 480px){
		.mcnImageGroupBlockOuter{
			padding-top:9px !important;
			padding-bottom:9px !important;
		}

}	@media only screen and (max-width: 480px){
		.mcnTextContent,.mcnBoxedTextContentColumn{
			padding-right:18px !important;
			padding-left:18px !important;
		}

}	@media only screen and (max-width: 480px){
		.mcnImageCardLeftImageContent,.mcnImageCardRightImageContent{
			padding-right:18px !important;
			padding-bottom:0 !important;
			padding-left:18px !important;
		}

}	@media only screen and (max-width: 480px){
		.mcpreview-image-uploader{
			display:none !important;
			width:100% !important;
		}

}	@media only screen and (max-width: 480px){
	/*
	@tab Mobile Styles
	@section Heading 1
	@tip Make the first-level headings larger in size for better readability on small screens.
	*/
		h1{
			/*@editable*/font-size:30px !important;
			/*@editable*/line-height:125% !important;
		}

}	@media only screen and (max-width: 480px){
	/*
	@tab Mobile Styles
	@section Heading 2
	@tip Make the second-level headings larger in size for better readability on small screens.
	*/
		h2{
			/*@editable*/font-size:26px !important;
			/*@editable*/line-height:125% !important;
		}

}	@media only screen and (max-width: 480px){
	/*
	@tab Mobile Styles
	@section Heading 3
	@tip Make the third-level headings larger in size for better readability on small screens.
	*/
		h3{
			/*@editable*/font-size:20px !important;
			/*@editable*/line-height:150% !important;
		}

}	@media only screen and (max-width: 480px){
	/*
	@tab Mobile Styles
	@section Heading 4
	@tip Make the fourth-level headings larger in size for better readability on small screens.
	*/
		h4{
			/*@editable*/font-size:18px !important;
			/*@editable*/line-height:150% !important;
		}

}	@media only screen and (max-width: 480px){
	/*
	@tab Mobile Styles
	@section Boxed Text
	@tip Make the boxed text larger in size for better readability on small screens. We recommend a font size of at least 16px.
	*/
		.mcnBoxedTextContentContainer .mcnTextContent,.mcnBoxedTextContentContainer .mcnTextContent p{
			/*@editable*/font-size:14px !important;
			/*@editable*/line-height:150% !important;
		}

}	@media only screen and (max-width: 480px){
	/*
	@tab Mobile Styles
	@section Header Text
	@tip Make the header text larger in size for better readability on small screens.
	*/
		.headerContainer .mcnTextContent,.headerContainer .mcnTextContent p{
			/*@editable*/font-size:16px !important;
			/*@editable*/line-height:150% !important;
		}

}	@media only screen and (max-width: 480px){
	/*
	@tab Mobile Styles
	@section Body Text
	@tip Make the body text larger in size for better readability on small screens. We recommend a font size of at least 16px.
	*/
		.bodyContainer .mcnTextContent,.bodyContainer .mcnTextContent p{
			/*@editable*/font-size:16px !important;
			/*@editable*/line-height:150% !important;
		}

}	@media only screen and (max-width: 480px){
	/*
	@tab Mobile Styles
	@section Footer Text
	@tip Make the footer content text larger in size for better readability on small screens.
	*/
		.footerContainer .mcnTextContent,.footerContainer .mcnTextContent p{
			/*@editable*/font-size:14px !important;
			/*@editable*/line-height:150% !important;
		}

}</style></head>
    <body>
       
        <center>
            <table align="center" border="0" cellpadding="0" cellspacing="0" height="100%" width="100%" id="bodyTable">
                <tr>
                    <td align="center" valign="top" id="bodyCell">
                        <!-- BEGIN TEMPLATE // -->
                        <table border="0" cellpadding="0" cellspacing="0" width="100%">
                            <tr>
                                <td align="center" valign="top" id="templateHeader" data-template-container>
                                    <!--[if (gte mso 9)|(IE)]>
                                    <table align="center" border="0" cellspacing="0" cellpadding="0" width="600" style="width:600px;">
                                    <tr>
                                    <td align="center" valign="top" width="600" style="width:600px;">
                                    <![endif]-->
                                    <table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" class="templateContainer">
                                        <tr>
                                            <td valign="top" class="headerContainer"><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width:100%;">
    <tbody class="mcnTextBlockOuter">
        <tr>
            <td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">
              	<!--[if mso]>
				<table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">
				<tr>
				<![endif]-->
			    
				<!--[if mso]>
				<td valign="top" width="600" style="width:600px;">
				<![endif]-->
                <table align="left" border="0" cellpadding="0" cellspacing="0" style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">
                    <tbody><tr>
                        
                        <td valign="top" class="mcnTextContent" style="padding: 0px 18px 9px;color: #FFFFFF;">
                        
                            <h1>New Christmas offers</h1>

                        </td>
                    </tr>
                </tbody></table>
				<!--[if mso]>
				</td>
				<![endif]-->
                
				<!--[if mso]>
				</tr>
				</table>
				<![endif]-->
            </td>
        </tr>
    </tbody>
</table></td>
                                        </tr>
                                    </table>
                                    <!--[if (gte mso 9)|(IE)]>
                                    </td>
                                    </tr>
                                    </table>
                                    <![endif]-->
                                </td>
                            </tr>
                            <tr>
                                <td align="center" valign="top" id="templateBody" data-template-container>
                                    <!--[if (gte mso 9)|(IE)]>
                                    <table align="center" border="0" cellspacing="0" cellpadding="0" width="600" style="width:600px;">
                                    <tr>
                                    <td align="center" valign="top" width="600" style="width:600px;">
                                    <![endif]-->
                                    <table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" class="templateContainer">
                                        <tr>
                                            <td valign="top" class="bodyContainer"><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnImageBlock" style="min-width:100%;">
    <tbody class="mcnImageBlockOuter">
            <tr>
                <td valign="top" style="padding:9px" class="mcnImageBlockInner">
                    <table align="left" width="100%" border="0" cellpadding="0" cellspacing="0" class="mcnImageContentContainer" style="min-width:100%;">
                        <tbody><tr>
                            <td class="mcnImageContent" valign="top" style="padding-right: 9px; padding-left: 9px; padding-top: 0; padding-bottom: 0; text-align:center;">
                                
                                    <a href="https://amzn.to/2Kc7Xn5" title="" class="" target="_blank">
                                        <img align="center" alt="" src="https://mcusercontent.com/0696b552530703b1e1a9285fa/images/df6bb60d-9a54-4df1-b7dc-8bb9b4dbadcb.jpg" width="271.70000000000005" style="max-width: 988px; padding-bottom: 0px; vertical-align: bottom; display: inline !important; border: 1px none;" class="mcnRetinaImage">
                                    </a>
                                
                            </td>
                        </tr>
                    </tbody></table>
                </td>
            </tr>
    </tbody>
</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width:100%;">
    <tbody class="mcnTextBlockOuter">
        <tr>
            <td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">
              	<!--[if mso]>
				<table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">
				<tr>
				<![endif]-->
			    
				<!--[if mso]>
				<td valign="top" width="600" style="width:600px;">
				<![endif]-->
                <table align="left" border="0" cellpadding="0" cellspacing="0" style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">
                    <tbody><tr>
                        
                        <td valign="top" class="mcnTextContent" style="padding-top:0; padding-right:18px; padding-bottom:9px; padding-left:18px;">
                        
                            <h3 dir="ltr" style="text-align: center;"><span style="font-family:tahoma,verdana,segoe,sans-serif"><span style="font-size:16px"><a href="https://amzn.to/2Kc7Xn5" target="_blank"><span class="mc-toc-title">Bluetooth Beanie Hat Gifts for Men, V5.0 Bluetooth Beanie Hat with Wireless Headphone Speaker for Him/Dad/Teens, Men's Tech Gift for Christmas Birthday Thanksgiving, Musical Cap for Stocking Stuffers.</span></a></span></span></h3>

                        </td>
                    </tr>
                </tbody></table>
				<!--[if mso]>
				</td>
				<![endif]-->
                
				<!--[if mso]>
				</tr>
				</table>
				<![endif]-->
            </td>
        </tr>
    </tbody>
</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnButtonBlock" style="min-width:100%;">
    <tbody class="mcnButtonBlockOuter">
        <tr>
            <td style="padding-top:0; padding-right:18px; padding-bottom:18px; padding-left:18px;" valign="top" align="center" class="mcnButtonBlockInner">
                <table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnButtonContentContainer" style="border-collapse: separate !important;border-radius: 9px;background-color: #434444;">
                    <tbody>
                        <tr>
                            <td align="center" valign="middle" class="mcnButtonContent" style="font-family: Helvetica; font-size: 18px; padding: 18px;">
                                <a class="mcnButton " title="Start Shopping" href="https://amzn.to/2Kc7Xn5" target="_blank" style="font-weight: bold;letter-spacing: normal;line-height: 100%;text-align: center;text-decoration: none;color: #FFFFFF;">Start Shopping</a>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </td>
        </tr>
    </tbody>
</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnDividerBlock" style="min-width:100%;">
    <tbody class="mcnDividerBlockOuter">
        <tr>
            <td class="mcnDividerBlockInner" style="min-width:100%; padding:18px;">
                <table class="mcnDividerContent" border="0" cellpadding="0" cellspacing="0" width="100%" style="min-width: 100%;border-top: 2px solid #EAEAEA;">
                    <tbody><tr>
                        <td>
                            <span></span>
                        </td>
                    </tr>
                </tbody></table>
<!--            
                <td class="mcnDividerBlockInner" style="padding: 18px;">
                <hr class="mcnDividerContent" style="border-bottom-color:none; border-left-color:none; border-right-color:none; border-bottom-width:0; border-left-width:0; border-right-width:0; margin-top:0; margin-right:0; margin-bottom:0; margin-left:0;" />
-->
            </td>
        </tr>
    </tbody>
</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnDividerBlock" style="min-width:100%;">
    <tbody class="mcnDividerBlockOuter">
        <tr>
            <td class="mcnDividerBlockInner" style="min-width:100%; padding:18px;">
                <table class="mcnDividerContent" border="0" cellpadding="0" cellspacing="0" width="100%" style="min-width:100%;">
                    <tbody><tr>
                        <td>
                            <span></span>
                        </td>
                    </tr>
                </tbody></table>
<!--            
                <td class="mcnDividerBlockInner" style="padding: 18px;">
                <hr class="mcnDividerContent" style="border-bottom-color:none; border-left-color:none; border-right-color:none; border-bottom-width:0; border-left-width:0; border-right-width:0; margin-top:0; margin-right:0; margin-bottom:0; margin-left:0;" />
-->
            </td>
        </tr>
    </tbody>
</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnCaptionBlock">
    <tbody class="mcnCaptionBlockOuter">
        <tr>
            <td class="mcnCaptionBlockInner" valign="top" style="padding:9px;">
                

<table border="0" cellpadding="0" cellspacing="0" class="mcnCaptionLeftContentOuter" width="100%">
    <tbody><tr>
        <td valign="top" class="mcnCaptionLeftContentInner" style="padding:0 9px 9px 9px ;">
            <table align="right" border="0" cellpadding="0" cellspacing="0" class="mcnCaptionLeftImageContentContainer" width="176">
                <tbody><tr>
                    <td class="mcnCaptionLeftImageContent" align="right" valign="top">
                    
                        
                        <a href="https://amzn.to/2WzXEvi" title="" class="" target="_blank">
                        
                        <img alt="" src="https://mcusercontent.com/0696b552530703b1e1a9285fa/images/b33dc6d5-7473-41fa-930d-b6d786703137.jpg" width="176" style="max-width: 300px;border: 1px none #B8B5B5;border-radius: 3%;" class="mcnImage">
                        </a>
                    
                    </td>
                </tr>
            </tbody></table>
            <table class="mcnCaptionLeftTextContentContainer" align="left" border="0" cellpadding="0" cellspacing="0" width="352">
                <tbody><tr>
                    <td valign="top" class="mcnTextContent" style="line-height: 100%;">
                        <h4><a href="https://amzn.to/2WzXEvi" target="_blank">Bose QuietComfort 35 II Wireless Bluetooth Headphones, Noise-Cancelling, with Alexa voice control - Black</a></h4>

                    </td>
                </tr>
            </tbody></table>
        </td>
    </tr>
</tbody></table>

<table border="0" cellpadding="0" cellspacing="0" class="mcnCaptionLeftContentOuter" width="100%">
    <tbody><tr>
        <td valign="top" class="mcnCaptionLeftContentInner" style="padding:9px 9px 0 9px ;">
            <table align="right" border="0" cellpadding="0" cellspacing="0" class="mcnCaptionLeftImageContentContainer" width="176">
                <tbody><tr>
                    <td class="mcnCaptionLeftImageContent" align="right" valign="top">
                    
                        
                        <a href="https://amzn.to/2WtnC3Q" title="" class="" target="_blank">
                        
                        <img alt="" src="https://mcusercontent.com/0696b552530703b1e1a9285fa/images/c6fa1638-86b0-4484-ae11-96987fc850ec.jpg" width="176" style="max-width: 200px;border: 1px none #B8B5B5;border-radius: 3%;" class="mcnImage">
                        </a>
                    
                    </td>
                </tr>
            </tbody></table>
            <table class="mcnCaptionLeftTextContentContainer" align="left" border="0" cellpadding="0" cellspacing="0" width="352">
                <tbody><tr>
                    <td valign="top" class="mcnTextContent" style="line-height: 100%;">
                        <h4><a href="https://amzn.to/2WtnC3Q" target="_blank">Bose Noise Cancelling Wireless Bluetooth Headphones 700, with Alexa Voice Control, Black</a></h4>

                    </td>
                </tr>
            </tbody></table>
        </td>
    </tr>
</tbody></table>





            </td>
        </tr>
    </tbody>
</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnDividerBlock" style="min-width:100%;">
    <tbody class="mcnDividerBlockOuter">
        <tr>
            <td class="mcnDividerBlockInner" style="min-width:100%; padding:18px;">
                <table class="mcnDividerContent" border="0" cellpadding="0" cellspacing="0" width="100%" style="min-width: 100%;border-top: 2px solid #EAEAEA;">
                    <tbody><tr>
                        <td>
                            <span></span>
                        </td>
                    </tr>
                </tbody></table>
<!--            
                <td class="mcnDividerBlockInner" style="padding: 18px;">
                <hr class="mcnDividerContent" style="border-bottom-color:none; border-left-color:none; border-right-color:none; border-bottom-width:0; border-left-width:0; border-right-width:0; margin-top:0; margin-right:0; margin-bottom:0; margin-left:0;" />
-->
            </td>
        </tr>
    </tbody>
</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnImageGroupBlock">
    <tbody class="mcnImageGroupBlockOuter">
        
            <tr>
                <td valign="top" style="padding:9px" class="mcnImageGroupBlockInner">
                    
                    <table align="left" width="273" border="0" cellpadding="0" cellspacing="0" class="mcnImageGroupContentContainer">
                            <tbody><tr>
                                <td class="mcnImageGroupContent" valign="top" style="padding-left: 9px; padding-top: 0; padding-bottom: 0;">
                                
                                    <a href="https://amzn.to/3nBcn5h" title="Star Wars The Child Animatronic Edition 7.2-Inch-Tall Toy by Hasbro with Over 25 Sound and Motion Combinations, Toys for Kids Ages 4 and Up" class="" target="_blank">
                                        <img alt="" src="https://mcusercontent.com/0696b552530703b1e1a9285fa/images/49331814-df31-4483-a760-66fa1ee71877.jpg" width="264" style="max-width: 300px;padding-bottom: 0px;border: 1px none #343434;border-radius: 0%;" class="mcnImage">
                                    </a>
                                
                                </td>
                            </tr>
                        </tbody></table>
                    
                    <table align="right" width="273" border="0" cellpadding="0" cellspacing="0" class="mcnImageGroupContentContainer">
                            <tbody><tr>
                                <td class="mcnImageGroupContent" valign="top" style="padding-right: 9px; padding-top: 0; padding-bottom: 0;">
                                
                                    <a href="https://amzn.to/2KLXmza" title="Star Wars The Black Series The Mandalorian Toy 6-Inch-Scale Collectible Action Figure, Toys for Kids Ages 4 and Up" class="" target="_blank">
                                        <img alt="" src="https://mcusercontent.com/0696b552530703b1e1a9285fa/images/a5666334-39d2-4a58-b0d0-811c4c910587.jpg" width="264" style="max-width: 300px;padding-bottom: 0px;border: 1px none #343434;border-radius: 0%;" class="mcnImage">
                                    </a>
                                
                                </td>
                            </tr>
                        </tbody></table>
                    
                </td>
            </tr>
        
    </tbody>
</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnImageGroupBlock">
    <tbody class="mcnImageGroupBlockOuter">
        
            <tr>
                <td valign="top" style="padding:9px" class="mcnImageGroupBlockInner">
                    
                    <table align="left" width="273" border="0" cellpadding="0" cellspacing="0" class="mcnImageGroupContentContainer">
                            <tbody><tr>
                                <td class="mcnImageGroupContent" valign="top" style="padding-left: 9px; padding-top: 0; padding-bottom: 0;">
                                
                                    <a href="https://amzn.to/3nF37gk" title="Bose QuietComfort Noise Cancelling Earbuds - True Wireless Earphones, Triple Black. The world's Most Effective Noise Cancelling Earbuds." class="" target="_blank">
                                        <img alt="" src="https://mcusercontent.com/0696b552530703b1e1a9285fa/images/92a6708c-c4a3-45a6-b065-72777cad6427.jpg" width="264" style="max-width:300px; padding-bottom: 0;" class="mcnImage">
                                    </a>
                                
                                </td>
                            </tr>
                        </tbody></table>
                    
                    <table align="right" width="273" border="0" cellpadding="0" cellspacing="0" class="mcnImageGroupContentContainer">
                            <tbody><tr>
                                <td class="mcnImageGroupContent" valign="top" style="padding-right: 9px; padding-top: 0; padding-bottom: 0;">
                                
                                    <a href="https://amzn.to/3h2SO3c" title="Apple AirPods Pro" class="" target="_blank">
                                        <img alt="" src="https://mcusercontent.com/0696b552530703b1e1a9285fa/images/f160392c-8542-49d0-98fd-24161ccd33ed.jpg" width="264" style="max-width:300px; padding-bottom: 0;" class="mcnImage">
                                    </a>
                                
                                </td>
                            </tr>
                        </tbody></table>
                    
                </td>
            </tr>
        
    </tbody>
</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnDividerBlock" style="min-width:100%;">
    <tbody class="mcnDividerBlockOuter">
        <tr>
            <td class="mcnDividerBlockInner" style="min-width:100%; padding:18px;">
                <table class="mcnDividerContent" border="0" cellpadding="0" cellspacing="0" width="100%" style="min-width: 100%;border-top: 2px solid #EAEAEA;">
                    <tbody><tr>
                        <td>
                            <span></span>
                        </td>
                    </tr>
                </tbody></table>
<!--            
                <td class="mcnDividerBlockInner" style="padding: 18px;">
                <hr class="mcnDividerContent" style="border-bottom-color:none; border-left-color:none; border-right-color:none; border-bottom-width:0; border-left-width:0; border-right-width:0; margin-top:0; margin-right:0; margin-bottom:0; margin-left:0;" />
-->
            </td>
        </tr>
    </tbody>
</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnImageCardBlock">
    <tbody class="mcnImageCardBlockOuter">
        <tr>
            <td class="mcnImageCardBlockInner" valign="top" style="padding-top:9px; padding-right:18px; padding-bottom:9px; padding-left:18px;">
                
<table align="left" border="0" cellpadding="0" cellspacing="0" class="mcnImageCardBottomContent" width="100%" style="border: 1px solid;">
    <tbody><tr>
        <td class="mcnImageCardBottomImageContent" align="right" valign="top" style="padding-top:18px; padding-right:18px; padding-bottom:0; padding-left:18px;">
        
            
            <a href="https://amzn.to/3awCS8a" title="Apple Watch Series 3 (GPS, 38mm) - Space Gray Aluminium Case with Black Sport Band" class="" target="_blank">
            

            <img alt="Apple Watch Series 3 (GPS, 38mm) - Space Gray Aluminium Case with Black Sport Band" src="https://mcusercontent.com/0696b552530703b1e1a9285fa/images/30c06ed1-058f-4bf9-afba-8c28620e219c.jpg" width="526" style="max-width: 1271px; border-radius: 0%;" class="mcnImage">
            </a>
        
        </td>
    </tr>
    <tr>
        <td class="mcnTextContent" valign="top" style="padding: 9px 18px;color: #F2F2F2;font-family: Helvetica;font-size: 14px;font-weight: normal;text-align: center;" width="528">
            <h1 id="title"><a href="https://amzn.to/3awCS8a" target="_blank"><em><span style="font-size:12px">Apple Watch Series 3 (GPS, 38mm) - Space Gray Aluminium Case with Black Sport Band</span></em></a></h1>

        </td>
    </tr>
</tbody></table>




            </td>
        </tr>
    </tbody>
</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnShareBlock" style="min-width:100%;">
    <tbody class="mcnShareBlockOuter">
            <tr>
                <td valign="top" style="padding:9px" class="mcnShareBlockInner">
                    <table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnShareContentContainer" style="min-width:100%;">
    <tbody><tr>
        <td align="center" style="padding-top:0; padding-left:9px; padding-bottom:0; padding-right:9px;">
            <table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="min-width: 100%; border: 1px none;" class="mcnShareContent">
                <tbody><tr>
                    <td align="center" valign="top" class="mcnShareContentItemContainer" style="padding-top:9px; padding-right:9px; padding-left:9px;">
                        <table align="center" border="0" cellpadding="0" cellspacing="0">
                            <tbody><tr>
                                <td align="left" valign="top">
                                    <!--[if mso]>
                                    <table align="center" border="0" cellspacing="0" cellpadding="0">
                                    <tr>
                                    <![endif]-->
                                    
                                        <!--[if mso]>
                                        <td align="center" valign="top">
                                        <![endif]-->
                                        <table align="left" border="0" cellpadding="0" cellspacing="0">
                                            <tbody><tr>
                                                <td valign="top" style="padding-right:9px; padding-bottom:9px;" class="mcnShareContentItemContainer">
                                                    <table border="0" cellpadding="0" cellspacing="0" width="" class="mcnShareContentItem" style="border-collapse: separate; border: 1px none; border-radius: 3.49462%;">
                                                        <tbody><tr>
                                                            <td align="left" valign="middle" style="padding-top:5px; padding-right:9px; padding-bottom:5px; padding-left:9px;">
                                                                <table align="left" border="0" cellpadding="0" cellspacing="0" width="">
                                                                    <tbody><tr>
                                                                        <td align="center" valign="middle" width="24" class="mcnShareIconContent">
                                                                            <a href="http://www.facebook.com/sharer/sharer.php?u=*|URL:ARCHIVE_LINK_SHORT|*" target="_blank"><img src="https://cdn-images.mailchimp.com/icons/social-block-v2/outline-dark-facebook-48.png" alt="Share" style="display:block;" height="24" width="24" class=""></a>
                                                                        </td>
                                                                        <td align="left" valign="middle" class="mcnShareTextContent" style="padding-left:5px;">
                                                                            <a href="http://www.facebook.com/sharer/sharer.php?u=*|URL:ARCHIVE_LINK_SHORT|*" target="" style="color: #202020;font-family: Georgia, Times, &quot;Times New Roman&quot;, serif;font-size: 12px;font-weight: normal;line-height: normal;text-align: center;text-decoration: none;">Share</a>
                                                                        </td>
                                                                    </tr>
                                                                </tbody></table>
                                                            </td>
                                                        </tr>
                                                    </tbody></table>
                                                </td>
                                            </tr>
                                        </tbody></table>
                                        <!--[if mso]>
                                        </td>
                                        <![endif]-->
                                    
                                        <!--[if mso]>
                                        <td align="center" valign="top">
                                        <![endif]-->
                                        <table align="left" border="0" cellpadding="0" cellspacing="0">
                                            <tbody><tr>
                                                <td valign="top" style="padding-right:9px; padding-bottom:9px;" class="mcnShareContentItemContainer">
                                                    <table border="0" cellpadding="0" cellspacing="0" width="" class="mcnShareContentItem" style="border-collapse: separate; border: 1px none; border-radius: 3.49462%;">
                                                        <tbody><tr>
                                                            <td align="left" valign="middle" style="padding-top:5px; padding-right:9px; padding-bottom:5px; padding-left:9px;">
                                                                <table align="left" border="0" cellpadding="0" cellspacing="0" width="">
                                                                    <tbody><tr>
                                                                        <td align="center" valign="middle" width="24" class="mcnShareIconContent">
                                                                            <a href="http://twitter.com/intent/tweet?text=*|URL:MC_SUBJECT|*: *|URL:ARCHIVE_LINK_SHORT|*" target="_blank"><img src="https://cdn-images.mailchimp.com/icons/social-block-v2/outline-dark-twitter-48.png" alt="Tweet" style="display:block;" height="24" width="24" class=""></a>
                                                                        </td>
                                                                        <td align="left" valign="middle" class="mcnShareTextContent" style="padding-left:5px;">
                                                                            <a href="http://twitter.com/intent/tweet?text=*|URL:MC_SUBJECT|*: *|URL:ARCHIVE_LINK_SHORT|*" target="" style="color: #202020;font-family: Georgia, Times, &quot;Times New Roman&quot;, serif;font-size: 12px;font-weight: normal;line-height: normal;text-align: center;text-decoration: none;">Tweet</a>
                                                                        </td>
                                                                    </tr>
                                                                </tbody></table>
                                                            </td>
                                                        </tr>
                                                    </tbody></table>
                                                </td>
                                            </tr>
                                        </tbody></table>
                                        <!--[if mso]>
                                        </td>
                                        <![endif]-->
                                    
                                        <!--[if mso]>
                                        <td align="center" valign="top">
                                        <![endif]-->
                                        <table align="left" border="0" cellpadding="0" cellspacing="0">
                                            <tbody><tr>
                                                <td valign="top" style="padding-right:9px; padding-bottom:9px;" class="mcnShareContentItemContainer">
                                                    <table border="0" cellpadding="0" cellspacing="0" width="" class="mcnShareContentItem" style="border-collapse: separate; border: 1px none; border-radius: 3.49462%;">
                                                        <tbody><tr>
                                                            <td align="left" valign="middle" style="padding-top:5px; padding-right:9px; padding-bottom:5px; padding-left:9px;">
                                                                <table align="left" border="0" cellpadding="0" cellspacing="0" width="">
                                                                    <tbody><tr>
                                                                        <td align="center" valign="middle" width="24" class="mcnShareIconContent">
                                                                            <a href="*|FORWARD|*" target="_blank"><img src="https://cdn-images.mailchimp.com/icons/social-block-v2/outline-dark-forwardtofriend-48.png" alt="Forward" style="display:block;" height="24" width="24" class=""></a>
                                                                        </td>
                                                                        <td align="left" valign="middle" class="mcnShareTextContent" style="padding-left:5px;">
                                                                            <a href="*|FORWARD|*" target="" style="color: #202020;font-family: Georgia, Times, &quot;Times New Roman&quot;, serif;font-size: 12px;font-weight: normal;line-height: normal;text-align: center;text-decoration: none;">Forward</a>
                                                                        </td>
                                                                    </tr>
                                                                </tbody></table>
                                                            </td>
                                                        </tr>
                                                    </tbody></table>
                                                </td>
                                            </tr>
                                        </tbody></table>
                                        <!--[if mso]>
                                        </td>
                                        <![endif]-->
                                    
                                        <!--[if mso]>
                                        <td align="center" valign="top">
                                        <![endif]-->
                                        <table align="left" border="0" cellpadding="0" cellspacing="0">
                                            <tbody><tr>
                                                <td valign="top" style="padding-right:9px; padding-bottom:9px;" class="mcnShareContentItemContainer">
                                                    <table border="0" cellpadding="0" cellspacing="0" width="" class="mcnShareContentItem" style="border-collapse: separate; border: 1px none; border-radius: 3.49462%;">
                                                        <tbody><tr>
                                                            <td align="left" valign="middle" style="padding-top:5px; padding-right:9px; padding-bottom:5px; padding-left:9px;">
                                                                <table align="left" border="0" cellpadding="0" cellspacing="0" width="">
                                                                    <tbody><tr>
                                                                        <td align="center" valign="middle" width="24" class="mcnShareIconContent">
                                                                            <a href="http://www.linkedin.com/shareArticle?url=*|URL:ARCHIVE_LINK_SHORT|*&amp;mini=true&amp;title=*|URL:MC_SUBJECT|*" target="_blank"><img src="https://cdn-images.mailchimp.com/icons/social-block-v2/outline-dark-linkedin-48.png" alt="Share" style="display:block;" height="24" width="24" class=""></a>
                                                                        </td>
                                                                        <td align="left" valign="middle" class="mcnShareTextContent" style="padding-left:5px;">
                                                                            <a href="http://www.linkedin.com/shareArticle?url=*|URL:ARCHIVE_LINK_SHORT|*&amp;mini=true&amp;title=*|URL:MC_SUBJECT|*" target="" style="color: #202020;font-family: Georgia, Times, &quot;Times New Roman&quot;, serif;font-size: 12px;font-weight: normal;line-height: normal;text-align: center;text-decoration: none;">Share</a>
                                                                        </td>
                                                                    </tr>
                                                                </tbody></table>
                                                            </td>
                                                        </tr>
                                                    </tbody></table>
                                                </td>
                                            </tr>
                                        </tbody></table>
                                        <!--[if mso]>
                                        </td>
                                        <![endif]-->
                                    
                                        <!--[if mso]>
                                        <td align="center" valign="top">
                                        <![endif]-->
                                        <table align="left" border="0" cellpadding="0" cellspacing="0">
                                            <tbody><tr>
                                                <td valign="top" style="padding-right:0; padding-bottom:9px;" class="mcnShareContentItemContainer">
                                                    <table border="0" cellpadding="0" cellspacing="0" width="" class="mcnShareContentItem" style="border-collapse: separate; border: 1px none; border-radius: 3.49462%;">
                                                        <tbody><tr>
                                                            <td align="left" valign="middle" style="padding-top:5px; padding-right:9px; padding-bottom:5px; padding-left:9px;">
                                                                <table align="left" border="0" cellpadding="0" cellspacing="0" width="">
                                                                    <tbody><tr>
                                                                        <td align="center" valign="middle" width="24" class="mcnShareIconContent">
                                                                            <a href="https://www.pinterest.com/pin/find/?url=*|URL:ARCHIVE_LINK_SHORT|*" target="_blank"><img src="https://cdn-images.mailchimp.com/icons/social-block-v2/outline-dark-pinterest-48.png" alt="Pin" style="display:block;" height="24" width="24" class=""></a>
                                                                        </td>
                                                                        <td align="left" valign="middle" class="mcnShareTextContent" style="padding-left:5px;">
                                                                            <a href="https://www.pinterest.com/pin/find/?url=*|URL:ARCHIVE_LINK_SHORT|*" target="" style="color: #202020;font-family: Georgia, Times, &quot;Times New Roman&quot;, serif;font-size: 12px;font-weight: normal;line-height: normal;text-align: center;text-decoration: none;">Pin</a>
                                                                        </td>
                                                                    </tr>
                                                                </tbody></table>
                                                            </td>
                                                        </tr>
                                                    </tbody></table>
                                                </td>
                                            </tr>
                                        </tbody></table>
                                        <!--[if mso]>
                                        </td>
                                        <![endif]-->
                                    
                                    <!--[if mso]>
                                    </tr>
                                    </table>
                                    <![endif]-->
                                </td>
                            </tr>
                        </tbody></table>
                    </td>
                </tr>
            </tbody></table>
        </td>
    </tr>
</tbody></table>

                </td>
            </tr>
    </tbody>
</table></td>
                                        </tr>
                                    </table>
                                    <!--[if (gte mso 9)|(IE)]>
                                    </td>
                                    </tr>
                                    </table>
                                    <![endif]-->
                                </td>
                            </tr>
                            <tr>
                                <td align="center" valign="top" id="templateFooter" data-template-container>
                                    <!--[if (gte mso 9)|(IE)]>
                                    <table align="center" border="0" cellspacing="0" cellpadding="0" width="600" style="width:600px;">
                                    <tr>
                                    <td align="center" valign="top" width="600" style="width:600px;">
                                    <![endif]-->
                                    <table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" class="templateContainer">
                                        <tr>
                                            <td valign="top" class="footerContainer"><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width:100%;">
    <tbody class="mcnTextBlockOuter">
        <tr>
            <td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">
              	<!--[if mso]>
				<table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">
				<tr>
				<![endif]-->
			    
				<!--[if mso]>
				<td valign="top" width="600" style="width:600px;">
				<![endif]-->
                <table align="left" border="0" cellpadding="0" cellspacing="0" style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">
                    <tbody><tr>
                        
                        <td valign="top" class="mcnTextContent" style="padding-top:0; padding-right:18px; padding-bottom:9px; padding-left:18px;">
                        
                            <em>Copyright © ajarmailer</em><br>
<strong>Our mailing address is:</strong><br>
ajar@mail.ajarmailer.ga<br>
<br>
Want to change how you receive these emails?<br>
You can&nbsp;<a href="https://forms.gle/V9zLHMZLTnWhBbDQ7" target="_blank">unsubscribe from this list</a>.<br>
<br>
Thank You
                        </td>
                    </tr>
                </tbody></table>
				<!--[if mso]>
				</td>
				<![endif]-->
                
				<!--[if mso]>
				</tr>
				</table>
				<![endif]-->
            </td>
        </tr>
    </tbody>
</table></td>
                                        </tr>
                                    </table>
                                    <!--[if (gte mso 9)|(IE)]>
                                    </td>
                                    </tr>
                                    </table>
                                    <![endif]-->
                                </td>
                            </tr>
                        </table>
                        <!-- // END TEMPLATE -->
                    </td>
                </tr>
            </table>
        </center>
    </body>
</html>

"""
 
# msg = email.message.Message()
msg = MIMEMultipart('alternative')
msg['Subject'] = 'Your Christmas and new years buying is here.'

 
msg['From'] = 'ajar@mail.ajarmailer.ga'
msg['To'] = 'ajar.shopinsta@gmail.com'
# password = "Raja@1802"
msg.add_header('Content-Type', 'text/html')
# msg.set_payload(email_content)
part2 = MIMEText(html, 'html')
msg.attach(part2)
s = smtplib.SMTP('smtp.localhost: 25')
s.starttls()
# Login Credentials for sending the mail
# s.login(msg['From'], password)
# msg = msg.as_string()
# msg = msg.encode('ascii', 'gnore').decode('ascii')
s.sendmail(msg['From'], [msg['To']], msg.as_string())


# In[ ]:




