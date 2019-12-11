#!/usr/bin/python3
# -*- coding: utf-8 -*-

# - - - - - - - - - - - - - - [ Bloco de Importar Bibliotecas (libs) ] - - - - - - - - - - - - - - #
try:
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email import encoders
    import os
    import os.path

except Exception as E:
    print(str(E))


# - - - - - - - - - - - - - - [ Bloco de Receber os Parametros (1o) ] - - - - - - - - - - - - - - #

# [ Recebe os Parametros ]
try:
    # Variavel que define se o Email possuira anexo ou nao ('T' / 'F')
    possuiAnexo = 'F'

    # SMTP Pelo qual sera efetuado o disparo
    smtphostname = 'sharedrelay-cluster.exemplo.net'
    username = 'exemplo@shared.exemplo.net'
    password = 'senha_exemplo'
    emailremetente = '<contato@exemplo.net>'  # Dentro do <> esta o email que sera dado como o remetente

except Exception as E:
    print(str(E))


# - - - - - - - - - - - - - - [ Bloco de Codigo da Execucao (2o) ] - - - - - - - - - - - - - - #

# [ Efetua conexao com o SMTP ]
try:
    server = smtplib.SMTP(smtphostname, 587)
    server.starttls()
    server.login(username, password)

except Exception as E:
    print(str(E))



# [ Define o Destino, a Mensagem, o Assunto e o Remetente do email ]
try:
    # Variavel do Email que sera disparado o Email
    emailremetente2 = ''

    # Obtem EMAIL do caso atual
    emailcliente = 'john.doe@exemplo.com.br'

    # Define a Mensagem, Assunto e Remetente do email
    message = "<html xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:o=\"urn:schemas-microsoft-com:office:office\" xmlns:v=\"urn:schemas-microsoft-com:vml\"> <head> <!--[if gte mso 9]><xml><o:OfficeDocumentSettings><o:AllowPNG/><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml><![endif]--> <meta content=\"text/html; charset=utf-8\" http-equiv=\"Content-Type\"/> <meta content=\"width=device-width\" name=\"viewport\"/> <!--[if !mso]><!--> <meta content=\"IE=edge\" http-equiv=\"X-UA-Compatible\"/><script type=\"text/javascript\">window.NREUM||(NREUM={}),__nr_require=function(e,n,t){function r(t){if(!n[t]){var o=n[t]={exports:{}};e[t][0].call(o.exports,function(n){var o=e[t][1][n];return r(o||n)},o,o.exports)}return n[t].exports}if(\"function\"==typeof __nr_require)return __nr_require;for(var o=0;o<t.length;o++)r(t[o]);return r}({1:[function(e,n,t){function r(){}function o(e,n,t){return function(){return i(e,[c.now()].concat(u(arguments)),n?null:this,t),n?void 0:this}}var i=e(\"handle\"),a=e(3),u=e(4),f=e(\"ee\").get(\"tracer\"),c=e(\"loader\"),s=NREUM;\"undefined\"==typeof window.newrelic&&(newrelic=s);var p=[\"setPageViewName\",\"setCustomAttribute\",\"setErrorHandler\",\"finished\",\"addToTrace\",\"inlineHit\",\"addRelease\"],d=\"api-\",l=d+\"ixn-\";a(p,function(e,n){s[n]=o(d+n,!0,\"api\")}),s.addPageAction=o(d+\"addPageAction\",!0),s.setCurrentRouteName=o(d+\"routeName\",!0),n.exports=newrelic,s.interaction=function(){return(new r).get()};var m=r.prototype={createTracer:function(e,n){var t={},r=this,o=\"function\"==typeof n;return i(l+\"tracer\",[c.now(),e,t],r),function(){if(f.emit((o?\"\":\"no-\")+\"fn-start\",[c.now(),r,o],t),o)try{return n.apply(this,arguments)}catch(e){throw f.emit(\"fn-err\",[arguments,this,e],t),e}finally{f.emit(\"fn-end\",[c.now()],t)}}}};a(\"actionText,setName,setAttribute,save,ignore,onEnd,getContext,end,get\".split(\",\"),function(e,n){m[n]=o(l+n)}),newrelic.noticeError=function(e,n){\"string\"==typeof e&&(e=new Error(e)),i(\"err\",[e,c.now(),!1,n])}},{}],2:[function(e,n,t){function r(e,n){if(!o)return!1;if(e!==o)return!1;if(!n)return!0;if(!i)return!1;for(var t=i.split(\".\"),r=n.split(\".\"),a=0;a<r.length;a++)if(r[a]!==t[a])return!1;return!0}var o=null,i=null,a=/Version\/(\S+)\s+Safari/;if(navigator.userAgent){var u=navigator.userAgent,f=u.match(a);f&&u.indexOf(\"Chrome\")===-1&&u.indexOf(\"Chromium\")===-1&&(o=\"Safari\",i=f[1])}n.exports={agent:o,version:i,match:r}},{}],3:[function(e,n,t){function r(e,n){var t=[],r=\"\",i=0;for(r in e)o.call(e,r)&&(t[i]=n(r,e[r]),i+=1);return t}var o=Object.prototype.hasOwnProperty;n.exports=r},{}],4:[function(e,n,t){function r(e,n,t){n||(n=0),\"undefined\"==typeof t&&(t=e?e.length:0);for(var r=-1,o=t-n||0,i=Array(o<0?0:o);++r<o;)i[r]=e[n+r];return i}n.exports=r},{}],5:[function(e,n,t){n.exports={exists:\"undefined\"!=typeof window.performance&&window.performance.timing&&\"undefined\"!=typeof window.performance.timing.navigationStart}},{}],ee:[function(e,n,t){function r(){}function o(e){function n(e){return e&&e instanceof r?e:e?f(e,u,i):i()}function t(t,r,o,i){if(!d.aborted||i){e&&e(t,r,o);for(var a=n(o),u=v(t),f=u.length,c=0;c<f;c++)u[c].apply(a,r);var p=s[y[t]];return p&&p.push([b,t,r,a]),a}}function l(e,n){h[e]=v(e).concat(n)}function m(e,n){var t=h[e];if(t)for(var r=0;r<t.length;r++)t[r]===n&&t.splice(r,1)}function v(e){return h[e]||[]}function g(e){return p[e]=p[e]||o(t)}function w(e,n){c(e,function(e,t){n=n||\"feature\",y[t]=n,n in s||(s[n]=[])})}var h={},y={},b={on:l,addEventListener:l,removeEventListener:m,emit:t,get:g,listeners:v,context:n,buffer:w,abort:a,aborted:!1};return b}function i(){return new r}function a(){(s.api||s.feature)&&(d.aborted=!0,s=d.backlog={})}var u=\"nr@context\",f=e(\"gos\"),c=e(3),s={},p={},d=n.exports=o();d.backlog=s},{}],gos:[function(e,n,t){function r(e,n,t){if(o.call(e,n))return e[n];var r=t();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(e,n,{value:r,writable:!0,enumerable:!1}),r}catch(i){}return e[n]=r,r}var o=Object.prototype.hasOwnProperty;n.exports=r},{}],handle:[function(e,n,t){function r(e,n,t,r){o.buffer([e],r),o.emit(e,n,t)}var o=e(\"ee\").get(\"handle\");n.exports=r,r.ee=o},{}],id:[function(e,n,t){function r(e){var n=typeof e;return!e||\"object\"!==n&&\"function\"!==n?-1:e===window?0:a(e,i,function(){return o++})}var o=1,i=\"nr@id\",a=e(\"gos\");n.exports=r},{}],loader:[function(e,n,t){function r(){if(!E++){var e=x.info=NREUM.info,n=l.getElementsByTagName(\"script\")[0];if(setTimeout(s.abort,3e4),!(e&&e.licenseKey&&e.applicationID&&n))return s.abort();c(y,function(n,t){e[n]||(e[n]=t)}),f(\"mark\",[\"onload\",a()+x.offset],null,\"api\");var t=l.createElement(\"script\");t.src=\"https://\"+e.agent,n.parentNode.insertBefore(t,n)}}function o(){\"complete\"===l.readyState&&i()}function i(){f(\"mark\",[\"domContent\",a()+x.offset],null,\"api\")}function a(){return O.exists&&performance.now?Math.round(performance.now()):(u=Math.max((new Date).getTime(),u))-x.offset}var u=(new Date).getTime(),f=e(\"handle\"),c=e(3),s=e(\"ee\"),p=e(2),d=window,l=d.document,m=\"addEventListener\",v=\"attachEvent\",g=d.XMLHttpRequest,w=g&&g.prototype;NREUM.o={ST:setTimeout,SI:d.setImmediate,CT:clearTimeout,XHR:g,REQ:d.Request,EV:d.Event,PR:d.Promise,MO:d.MutationObserver};var h=\"\"+location,y={beacon:\"bam.nr-data.net\",errorBeacon:\"bam.nr-data.net\",agent:\"js-agent.newrelic.com/nr-1130.min.js\"},b=g&&w&&w[m]&&!/CriOS/.test(navigator.userAgent),x=n.exports={offset:u,now:a,origin:h,features:{},xhrWrappable:b,userAgent:p};e(1),l[m]?(l[m](\"DOMContentLoaded\",i,!1),d[m](\"load\",r,!1)):(l[v](\"onreadystatechange\",o),d[v](\"onload\",r)),f(\"mark\",[\"firstbyte\",u],null,\"api\");var E=0,O=e(5)},{}]},{},[\"loader\"]);</script> <!--<![endif]--> <title></title> <!--[if !mso]><!--> <link href=\"https://fonts.googleapis.com/css?family=Montserrat\" rel=\"stylesheet\" type=\"text/css\"/> <!--<![endif]--> <style type=\"text/css\"> 		body { 			margin: 0; 			padding: 0; 		}  		table, 		td, 		tr { 			vertical-align: top; 			border-collapse: collapse; 		}  		* { 			line-height: inherit; 		}  		a[x-apple-data-detectors=true] { 			color: inherit !important; 			text-decoration: none !important; 		} 	</style> <style id=\"media-query\" type=\"text/css\"> 		@media (max-width: 620px) {  			.block-grid, 			.col { 				min-width: 320px !important; 				max-width: 100% !important; 				display: block !important; 			}  			.block-grid { 				width: 100% !important; 			}  			.col { 				width: 100% !important; 			}  			.col>div { 				margin: 0 auto; 			}  			img.fullwidth, 			img.fullwidthOnMobile { 				max-width: 100% !important; 			}  			.no-stack .col { 				min-width: 0 !important; 				display: table-cell !important; 			}  			.no-stack.two-up .col { 				width: 50% !important; 			}  			.no-stack .col.num4 { 				width: 33% !important; 			}  			.no-stack .col.num8 { 				width: 66% !important; 			}  			.no-stack .col.num4 { 				width: 33% !important; 			}  			.no-stack .col.num3 { 				width: 25% !important; 			}  			.no-stack .col.num6 { 				width: 50% !important; 			}  			.no-stack .col.num9 { 				width: 75% !important; 			}  			.video-block { 				max-width: none !important; 			}  			.mobile_hide { 				min-height: 0px; 				max-height: 0px; 				max-width: 0px; 				display: none; 				overflow: hidden; 				font-size: 0px; 			}  			.desktop_hide { 				display: block !important; 				max-height: none !important; 			} 		} 	</style> </head> <body class=\"clean-body\" style=\"margin: 0; padding: 0; -webkit-text-size-adjust: 100%; background-color: #ACACAC;\"> </body> </html>"
    subject = 'Informativo'
    emailremetente2 = 'Informacoes ' + emailremetente  # O nome que irá aparecer no Email + o email que sera dado como o remetente

except Exception as E:
    print(str(E))



# [ Obtem o Anexo e Monta o Email COM ANEXO ]
if possuiAnexo == 'T':

    # Obtem o Anexo
    try:
        file_location = os.path.join('_PDFs', 'anexo_exemplo.pdf')

    except Exception as E:
        print(str(E))


    # Monta o Email
    try:
        # Define a mensagem como MIMEMultipart, isso é necessario para anexar arquivos
        msg = MIMEMultipart()
        msg['From'] = emailremetente2
        msg['To'] = emailcliente
        msg['Subject'] = subject

        # Anexando o corpo do texto ao MIMEMultipart
        msg.attach(MIMEText(message, 'html'))

        # Fazendo o setup necessario para o anexo
        filename = os.path.basename(file_location)
        attachment = open(file_location, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        # Anexando o arquivo ao objeto MIMEMultipart
        msg.attach(part)

    except Exception as E:
        print(str(E))



# [ Monta o Email SEM ANEXO ]
elif possuiAnexo == 'F':

    # Monta o Email
    try:
        # Define a mensagem como MIMEMultipart
        msg = MIMEMultipart()
        msg['From'] = emailremetente2
        msg['To'] = emailcliente
        msg['Subject'] = subject

        # Anexando o corpo do texto ao MIMEMultipart
        msg.attach(MIMEText(message, 'html'))

    except Exception as E:
        print(str(E))



# [ Envia o Email ]
try:
    # Transformando o MIMEMultipart em texto para poder enviar pelo e-mail
    text = msg.as_string()
    server.sendmail(emailremetente2, emailcliente, text)

except (Exception, smtplib.SMTPException, smtplib.SMTPServerDisconnected, smtplib.SMTPResponseException, smtplib.SMTPSenderRefused, smtplib.SMTPRecipientsRefused, smtplib.SMTPDataError, smtplib.SMTPConnectError, smtplib.SMTPHeloError, smtplib.SMTPNotSupportedError, smtplib.SMTPAuthenticationError) as E:
    print(str(E))



# [ Finaliza a conexao com o SMTP ]
try:
    server.quit()

except Exception as E:
    print(str(E))
