def plotInstance() :
    """
        Plot a single instance of the elevation, slope, curvature and glint, for
        comparison purposes.
    """

    #left  = 0.125  # the left side of the subplots of the figure
    #right = 0.9    # the right side of the subplots of the figure
    #bottom = 0.1   # the bottom of the subplots of the figure
    #top = 0.9      # the top of the subplots of the figure
    #wspace = 0.2   # the amount of width reserved for blank space between subplots
    #hspace = 0.2   # the amount of height reserved for white space between subplots

    pl.figure(figsize=(12,10))
    pl.subplots_adjust(left=0.05,right=0.95,bottom=0.05,top=0.95,wspace=0.15,hspace=0.15)

    #pl.subplot(4,1,1)
    #pl.plot(Scale.x,totalElevSurface.real,label="Elevation")
    #pl.xlim(11.,12.)
    #pl.ylim(-0.0005,0.005)
    #pl.legend()
    #pl.show()

    pl.subplot(4,1,1)
    testAng = 0
    slopeMin = Geom.xi_min[testAng]
    slopeMax = Geom.xi_max[testAng]
    pl.plot(Scale.x,totalSlopeSurface.real,label="Slope")
    pl.plot(Scale.x,np.ones(N)*slopeMin,label="Slope Min")
    pl.plot(Scale.x,np.ones(N)*slopeMax,label="Slope Max")
    #pl.plot(Scale.x,np.gradient(totalElevSurface.real,delta_x),label="Slope (gradient)")
    #pl.plot(Scale.x[:-1],np.diff(totalElevSurface.real,n=1)/delta_x,label="Slope (diff)")
    #pl.plot(Scale.x[:-1],np.diff(totalElevSurface.real,n=1)/delta_x,label="Slope (diff)")
    pl.xlim(20.,30.)
    #pl.ylim(-0.0005,0.005)
    pl.legend()
    pl.grid(b=True)
    pl.show()

    glint = np.double(totalSlopeSurface.real > slopeMin) * np.double(totalSlopeSurface.real < slopeMax)

    pl.subplot(4,1,2)
    pl.plot(Scale.x,glint,label="Glint")
    pl.xlim(20.,30.)
    pl.ylim(-0.2,1.2)
    pl.grid(b=True)
    pl.legend()
    pl.show()

    filterLen=64
    filterStdev = 0.6
    convX = np.linspace(-5.,5.,filterLen)
    convFilter = exp(-0.5*(convX**2.)/(filterStdev**2.))
    glintConv = np.convolve(glint,convFilter,mode='same')
    glintConv = (glintConv<=1.)*glintConv + (glintConv>1.)
    SLmag,SLstdev = 0.5,1./sqrt(200.)
    Skylight = SLmag*exp(-0.5*((totalSlopeSurface.real - Geom.xi_0[testAng])**2.)/(SLstdev**2.))
    combGlint = (glintConv > Skylight)*glintConv + (glintConv < Skylight)*Skylight

    pl.subplot(4,1,3)
    pl.plot(Scale.x,combGlint,label="Combined Glint")
    pl.xlim(20.,30.)
    pl.ylim(-0.2,1.2)
    pl.grid(b=True)
    pl.legend()
    pl.show()

    threshold = 0.45
    thresholdGlint = (combGlint >= threshold)*combGlint

    pl.subplot(4,1,4)
    pl.plot(Scale.x,thresholdGlint,label="Thresholded Glint")
    pl.xlim(20.,30.)
    pl.ylim(-0.2,1.2)
    pl.legend()
    pl.grid(b=True)
    pl.show()

    nbins = 100
    bins = np.linspace(0.,1.,nbins)
    pl.figure()
    glintHistogram = np.histogram(glint,bins,normed=True)
    pl.plot(bins[:-1],glintHistogram[0],label="Glint")
    glintHistogram = np.histogram(combGlint,bins,normed=True)
    pl.plot(bins[:-1],glintHistogram[0],label="Combined Glint")
    glintHistogram = np.histogram(thresholdGlint,bins,normed=True)
    pl.plot(bins[:-1],glintHistogram[0],label="Thresholded Glint")
    pl.xlim(-0.1,1.1)
    pl.ylim(-1.,10.)
    pl.legend()
    pl.show()

    #pl.subplot(4,1,4)
    #pl.plot(Scale.x,totalCurvatureSurface,label=r"$\eta^{''}(x)$")
    #pl.plot(Scale.x,np.gradient(np.gradient(totalElevSurface.real))/(delta_x*delta_x),label=r"$\eta^{''}(x)$ (gradient)")
    #pl.plot(Scale.x[1:-1],np.diff(totalElevSurface.real,n=2)/(delta_x**2.),label="$\eta^{''}(x)$ (diff)")
    #pl.plot(Scale.x,totalCurvatureSurface/(sqrt(1. + totalSlopeSurface**2.)**3.),label=r"$\kappa(x)$")
    #pl.plot(Scale.x[1:-1],(np.diff(totalElevSurface.real,n=2)/(delta_x**2.),label="Curvature (diff)")
    #pl.xlim(11.,12.)
    #pl.ylim(-0.0005,0.005)
    #pl.legend()
    #pl.grid(b=True)
    #pl.show()


    #return

    #left  = 0.125  # the left side of the subplots of the figure
    #right = 0.9    # the right side of the subplots of the figure
    #bottom = 0.1   # the bottom of the subplots of the figure
    #top = 0.9      # the top of the subplots of the figure
    #wspace = 0.2   # the amount of width reserved for blank space between subplots
    #hspace = 0.2   # the amount of height reserved for white space between subplots

    #pl.figure(figsize=(15,12))
    #pl.subplot(2,3,1)
    #pl.subplots_adjust(left=0.05,right=0.95,bottom=0.05,top=0.95,wspace=0.15,hspace=0.15)
    #pl.plot(Scale.k,ElevPower.primaryPower,label="primary")
    #pl.plot(Scale.k,ElevPower.nlPower,label="nonLinear")
    #pl.plot(Scale.k,ElevPower.totalPower,label="total")
    #pl.xlim(0.,5.)
    #pl.ylim(-0.0005,0.005)
    #pl.legend()
    #pl.title("Elevation Power Spectrum")
    #pl.show()

    #pl.subplot(2,3,2)
    #pl.plot(Scale.k,SlopePower.primaryPower,label="primary")
    #pl.plot(Scale.k,SlopePower.nlPower,label="nonLinear")
    #pl.plot(Scale.k,SlopePower.totalPower,label="total")
    #pl.xlim(0.,5.)
    #pl.ylim(-0.0005,0.005)
    #pl.legend()
    #pl.title("Slope Power Spectrum")
    #pl.show()

    #pl.subplot(2,3,3)
    #pl.plot(Scale.k,CurvaturePower.primaryPower,label="primary")
    #pl.plot(Scale.k,CurvaturePower.nlPower,label="nonLinear")
    #pl.plot(Scale.k,CurvaturePower.totalPower,label="total")
    #pl.xlim(0.,5.)
    #pl.ylim(-0.0005,0.005)
    #pl.legend()
    #pl.title("Curvature Power Spectrum")
    #pl.show()

    #pl.subplot(2,3,4)
    #pl.plot(Scale.k,2.*totalElevAvgPower/(delta_k*N_r),label="total")
    #pl.xlim(0.,5.)
    #pl.ylim(-0.0005,0.005)
    #pl.legend()
    #pl.title("Average Elevation Power Spectrum")
    #pl.show()

    #pl.subplot(2,3,5)
    #pl.plot(Scale.k,2.*totalSlopeAvgPower/(delta_k*N_r),label="total")
    #pl.xlim(0.,5.)
    #pl.ylim(-0.0005,0.005)
    #pl.legend()
    #pl.title("Average Slope Power Spectrum")
    #pl.show()

    #pl.subplot(2,3,6)
    #pl.plot(Scale.k,2.*totalCurvatureAvgPower/(delta_k*N_r),label="total")
    #pl.xlim(0.,5.)
    #pl.ylim(-0.0005,0.005)
    #pl.legend()
    #pl.title("Average Curvature Power Spectrum")
    #pl.show()


"""

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; Routine to return the glint cumulants from the glint moment(s), for 
;;; a number of geometries
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

PRO glintCumulantsFromMoments,glintMoments,glintCumulants

	PRINT,'N_ELEMENTS: ',N_ELEMENTS(glintCumulants[0,*])
	FOR geometry=0L,N_ELEMENTS(glintCumulants[0,*])-1L DO BEGIN
		glintCumulants[0,geometry] = glintMoments[geometry]
		glintCumulants[1,geometry] = glintMoments[geometry]-glintMoments[geometry]^2.D
		glintCumulants[2,geometry] = glintMoments[geometry] $
			-3.D*glintMoments[geometry]^2.D $
			+2.D*glintMoments[geometry]^3.D
	ENDFOR
;	glintCumulants[*,0] = glintMoments[*]
;	glintCumulants[*,1] = glintMoments[*]-glintMoments[*]^2.D
;	glintCumulants[*,2] = glintMoments[*]-3.D*glintMoments[*]*glintMoments[*]+2.D*glintMoments[*]^3.D
END

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; Routine to return the cumulants from the moments
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

PRO cumulantsFromMoments,dataMoments,dataCumulants

	dataCumulants[0] = dataMoments[0]
	dataCumulants[1] = dataMoments[1]-dataMoments[0]^2.D
	dataCumulants[2] = dataMoments[2]-3.D*dataMoments[0]*dataMoments[1]+2.D*dataMoments[0]^3.D

END

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; Routine to use the symmetry properties of the bispectrum of a real 
;;; sequence to populate an entire NxN array from the primary octant. Takes
;;; as input an NxN complex array, and the array size N, and returns the 
;;; fully populated array in the input array
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

PRO bispectrumSymmetry,bispectrum,N

	FOR j=0L,N/4L DO BEGIN
		FOR i=j,(N/2L-j) DO BEGIN
			bispectrum[(j LT 0L) ? N+(j) : j , (i LT 0L) ? N+(i) : i] = bispectrum[i,j]
			bispectrum[(j LT 0L) ? N+(j) : j , (-i-j LT 0L) ? N+(-i-j) : -i-j] = bispectrum[i,j]
			bispectrum[(-i-j LT 0L) ? N+(-i-j) : -i-j , (j LT 0L) ? N+(j) : j] = bispectrum[i,j]
			bispectrum[(-i-j LT 0L) ? N+(-i-j) : -i-j , (i LT 0L) ? N+(i) : i] = bispectrum[i,j]
			bispectrum[(i LT 0L) ? N+(i) : i , (-i-j LT 0L) ? N+(-i-j) : -i-j] = bispectrum[i,j]

			bispectrum[(-i LT 0L) ? N+(-i) : -i , (-j LT 0L) ? N+(-j) : -j   ] = CONJ(bispectrum[i,j])
			bispectrum[(-j LT 0L) ? N+(-j) : -j , (-i LT 0L) ? N+(-i) : -i   ] = CONJ(bispectrum[i,j])
			bispectrum[(-j LT 0L) ? N+(-j) : -j , (i+j LT 0L) ? N+(i+j) : i+j] = CONJ(bispectrum[i,j])
			bispectrum[(i+j LT 0L) ? N+(i+j) : i+j , (-j LT 0L) ? N+(-j) : -j] = CONJ(bispectrum[i,j])
			bispectrum[(i+j LT 0L) ? N+(i+j) : i+j , (-i LT 0L) ? N+(-i) : -i] = CONJ(bispectrum[i,j])
			bispectrum[(-i LT 0L) ? N+(-i) : -i , (i+j LT 0L) ? N+(i+j) : i+j] = CONJ(bispectrum[i,j])
		ENDFOR
	ENDFOR
END

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; Routine to use the symmetry properties of the bispectrum of a real 
;;; sequence to populate an entire NxN bicoherence array from the primary 
;;; octant. Takes as input an NxN real array, and the array size N, and 
;;; returns the fully populated array in the input array
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

PRO bicoherenceSymmetry,bicoherence,N

	FOR j=0L,N/4L DO BEGIN
		FOR i=j,(N/2L-j) DO BEGIN
			bicoherence[(j LT 0L) ? N+(j) : j , (i LT 0L) ? N+(i) : i] = bicoherence[i,j]
			bicoherence[(j LT 0L) ? N+(j) : j , (-i-j LT 0L) ? N+(-i-j) : -i-j] = bicoherence[i,j]
			bicoherence[(-i-j LT 0L) ? N+(-i-j) : -i-j , (j LT 0L) ? N+(j) : j] = bicoherence[i,j]
			bicoherence[(-i-j LT 0L) ? N+(-i-j) : -i-j , (i LT 0L) ? N+(i) : i] = bicoherence[i,j]
			bicoherence[(i LT 0L) ? N+(i) : i , (-i-j LT 0L) ? N+(-i-j) : -i-j] = bicoherence[i,j]

			bicoherence[(-i LT 0L) ? N+(-i) : -i , (-j LT 0L) ? N+(-j) : -j   ] = bicoherence[i,j]
			bicoherence[(-j LT 0L) ? N+(-j) : -j , (-i LT 0L) ? N+(-i) : -i   ] = bicoherence[i,j]
			bicoherence[(-j LT 0L) ? N+(-j) : -j , (i+j LT 0L) ? N+(i+j) : i+j] = bicoherence[i,j]
			bicoherence[(i+j LT 0L) ? N+(i+j) : i+j , (-j LT 0L) ? N+(-j) : -j] = bicoherence[i,j]
			bicoherence[(i+j LT 0L) ? N+(i+j) : i+j , (-i LT 0L) ? N+(-i) : -i] = bicoherence[i,j]
			bicoherence[(-i LT 0L) ? N+(-i) : -i , (i+j LT 0L) ? N+(i+j) : i+j] = bicoherence[i,j]
		ENDFOR
	ENDFOR
END
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; Routine to use the symmetry properties of the bicovariance of a real 
;;; sequence to populate an entire NxN array from the primary sextant. Takes
;;; as input an NxN complex array, and the array size N, and returns the 
;;; fully populated array in the input array
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

PRO biCovarianceSymmetry,biCovariance,N

	FOR i=0L,N/2L DO BEGIN
		FOR j=0L,i DO BEGIN
			biCovariance[(j LT 0L) ? N+(j) : j , (i LT 0L) ? N+(i) : i] = biCovariance[i,j]
			biCovariance[(-j LT 0L) ? N+(-j) : -j , (i-j LT 0L) ? N+(i-j) : i-j] = biCovariance[i,j]
			biCovariance[(i-j LT 0L) ? N+(i-j) : i-j , (-j LT 0L) ? N+(-j) : -j] = biCovariance[i,j]
			biCovariance[(j-i LT 0L) ? N+(j-i) : j-i , (-i LT 0L) ? N+(-i) : -i] = biCovariance[i,j]
			biCovariance[(-i LT 0L) ? N+(-i) : -i , (j-i LT 0L) ? N+(j-i) : j-i] = biCovariance[i,j]
		ENDFOR
	ENDFOR
END

"""

