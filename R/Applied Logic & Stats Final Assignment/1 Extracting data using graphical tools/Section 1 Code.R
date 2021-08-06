sids<- data.frame(read.csv("C:\\Users\\Yevgeniya Litvinova\\Documents\\SIW 004 Math and Stats\\final individual\\final_data.csv"))
#
sids <- sids[,-1]
attach(sids)
#
pairs(sids,panel=function(x,y) {abline(lsfit(x,y)$coef,lwd=2, col=2)
                                lines(lowess(x,y),lty=2,lwd=2, col=3)
                                points(x,y)})
cor(sids)
#
#
par(mfrow=c(2,2))
par(pty="s")		#s stands for plotting in the square window
plot(Gesage,BW,pch=1,lwd=2)
title("(a)",lwd=2)
plot(Gesage,BW,pch=1,lwd=2)
abline(lm(BW~Gesage),lwd=2)	#lm - linear model - Mortality = beta0(intercept) + beta1(slope)*SO2
						#abline - adds a line to an existing plot
title("(b)",lwd=2)
airpoll1<-jitter(cbind(Gesage,BW)) #jitter = shift the data a little bit (use only for graphical purpose) 
plot(airpoll1[,1],airpoll1[,2],xlab="Gesage",ylab="BW",pch=1,lwd=2)
title("(c)",lwd=2)
plot(Gesage,BW,pch=1,lwd=2)
rug(jitter(Gesage),side=1)			#gives density information within the existing plot
rug(jitter(BW),side=2)
title("(d)",lwd=2)
#
names<-abbreviate(row.names(sids))
par(mfrow=c(1,1))
plot(Gesage,BW,lwd=2,type="n")
text(Gesage,BW,labels=names,lwd=2)
#
#
dev.off()
#
par(fig=c(0,0.7,0,0.7))
plot(Gesage,BW,lwd=2)
abline(lm(BW~Gesage),lwd=2)
lines(lowess(Gesage,BW),lwd=2) 	#local weighted regression 
par(fig=c(0,0.7,0.65,1),new=TRUE)
#
hist(Gesage,lwd=2)
par(fig=c(0.65,1,0,0.7),new=TRUE)
boxplot(BW,lwd=2)
#
dev.off()
#
hull<-chull(Gesage,BW) #to draw a polygon with boundaries for point
plot(Gesage,BW,pch=1)
polygon(Gesage[hull],BW[hull],density=15,angle=30)
cor(Gesage,BW)
cor(Gesage[-hull],BW[-hull])
#
dev.off()
#
chiplot(Gesage,BW,vlabs=c("Gesage","BW"))
#
dev.off()
#
bvbox(cbind(Gesage,BW),xlab="Gesage",ylab="BW")
#
bvbox(cbind(Gesage,BW),xlab="Gesage",ylab="BW",method="O")
#
#
h2d<-hist2d(Gesage,BW)
persp(h2d,xlab="Gesage",ylab="BW",zlab="Frequency")
#
#
den1<-bivden(Gesage,BW)
persp(den1$seqx,den1$seqy,den1$den,xlab="Gesage",ylab="BW",
zlab="Density",lwd=2, theta = 0, phi = 30) #theta (azimuthal angle) and phi (vision angle) give different viewing perspectives
#
plot(Gesage,BW)
contour(den1$seqx,den1$seqy,den1$den,lwd=2,nlevels=20,add=TRUE)
#

# additional info on plot(Gesage,BW,pch=1,lwd=2,ylim=c(1500,5000),xlim=c(36,43))
symbols(Gesage,BW,circles=Factor68,inches=0.4,add=TRUE,lwd=2)Rainfall
pairs(airpoll)
#
pairs(sids,panel=function(x,y) {abline(lsfit(x,y)$coef,lwd=2)
                                  lines(lowess(x,y),lty=2,lwd=2)
                                  points(x,y)})
#to add a straight horizontal/vertical line to the plot


#
coplot(BW~Gesage|Factor68)
#
coplot(BW~Gesage|Factor68,panel=function(x,y,col,pch)
 panel.smooth(x,y,span=1))
#
