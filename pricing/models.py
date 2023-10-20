from django.db import models


class ProgramPricing(models.Model):
    program_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='destinations/images/')

    def __str__(self):
        return self.program_name

class ProgramDates(models.Model):
    program = models.ForeignKey(ProgramPricing, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.program.program_name

class ProgramFees(models.Model):
    program = models.ForeignKey(ProgramPricing, on_delete=models.CASCADE)
    tuition = models.DecimalField(max_digits=10, decimal_places=2)
    housing = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.program.program_name

class ProgramDetails(models.Model):
    program = models.ForeignKey(ProgramPricing, on_delete=models.CASCADE)
    program_description = models.TextField()

    def __str__(self):
        return self.program.program_name

class ProgramItinerary(models.Model):
    program = models.ForeignKey(ProgramPricing, on_delete=models.CASCADE)
    itinerary_description = models.TextField()

    def __str__(self):
        return self.program.program_name

class ProgramInclusions(models.Model):
    program = models.ForeignKey(ProgramPricing, on_delete=models.CASCADE)
    inclusions_description = models.TextField()

    def __str__(self):
        return self.program.program_name

class ProgramExclusions(models.Model):
    program = models.ForeignKey(ProgramPricing, on_delete=models.CASCADE)
    exclusions_description = models.TextField()

    def __str__(self):
        return self.program.program_name

class ProgramRequirements(models.Model):
    program = models.ForeignKey(ProgramPricing, on_delete=models.CASCADE)
    requirements_description = models.TextField()

    def __str__(self):
        return self.program.program_name

class ProgramVisa(models.Model):
    program = models.ForeignKey(ProgramPricing, on_delete=models.CASCADE)
    visa_description = models.TextField()

    def __str__(self):
        return self.program.program_name

class ProgramInsurance(models.Model):
    program = models.ForeignKey(ProgramPricing, on_delete=models.CASCADE)
    insurance_description = models.TextField()

    def __str__(self):
        return self.program.program_name

class ProgramCancellation(models.Model):
    program = models.ForeignKey(ProgramPricing, on_delete=models.CASCADE)
    cancellation_description = models.TextField()

    def __str__(self):
        return self.program.program_name

class ProgramRefund(models.Model):
    program = models.ForeignKey(ProgramPricing, on_delete=models.CASCADE)
    refund_description = models.TextField()

    def __str__(self):
        return self.program.program_name

class ProgramPayment(models.Model):
    program = models.ForeignKey(ProgramPricing, on_delete=models.CASCADE)
    payment_description = models.TextField()

    def __str__(self):
        return self.program.program_name

class ProgramTerms(models.Model):
    program = models.ForeignKey(ProgramPricing, on_delete=models.CASCADE)
    terms_description = models.TextField()

    def __str__(self):
        return self.program.program_name

class ProgramFAQ(models.Model):
    program = models.ForeignKey(ProgramPricing, on_delete=models.CASCADE)
    faq_description = models.TextField()

    def __str__(self):
        return self.program.program_name

class ProgramTestimonials(models.Model):
    program = models.ForeignKey(ProgramPricing, on_delete=models.CASCADE)
    testimonials_description = models.TextField()

    def __str__(self):
        return self.program.program_name
    
class ProgramGallery(models.Model):
    program = models.ForeignKey(ProgramPricing, on_delete=models.CASCADE)
    gallery_description = models.TextField()

    def __str__(self):
        return self.program.program_name

class ProgramGalleryImage(models.Model):
    program = models.ForeignKey(ProgramPricing, on_delete=models.CASCADE)
    gallery_image = models.ImageField(upload_to='destinations/images/')

    def __str__(self):
        return self.program.program_name

class ProgramDestination(models.Model):
    program = models.ForeignKey(ProgramPricing, on_delete=models.CASCADE)
    destination_description = models.TextField()

    def __str__(self):
        return self.program.program_name

class ProgramDestinationImage(models.Model):
    program = models.ForeignKey(ProgramPricing, on_delete=models.CASCADE)
    destination_image = models.ImageField(upload_to='destinations/images/')

    def __str__(self):
        return self.program.program_name
    
class ProgramDestinationVideo(models.Model):
    program = models.ForeignKey(ProgramPricing, on_delete=models.CASCADE)
    destination_video = models.FileField(upload_to='destinations/videos/')

    def __str__(self):
        return self.program.program_name

class ProgramDestinationMap(models.Model):
    program = models.ForeignKey(ProgramPricing, on_delete=models.CASCADE)
    destination_map = models.ImageField(upload_to='destinations/images/')

    def __str__(self):
        return self.program.program_name

class ProgramDestinationMapLink(models.Model):
    program = models.ForeignKey(ProgramPricing, on_delete=models.CASCADE)
    destination_map_link = models.TextField()

    def __str__(self):
        return self.program.program_name

class ProgramDestinationMapDescription(models.Model):
    program = models.ForeignKey(ProgramPricing, on_delete=models.CASCADE)
    destination_map_description = models.TextField()

    def __str__(self):
        return self.program.program_name

class ProgramDestinationMapImage(models.Model):
    program = models.ForeignKey(ProgramPricing, on_delete=models.CASCADE)
    destination_map_image = models.ImageField(upload_to='destinations/images/')

    def __str__(self):
        return self.program.program_name

class ProgramDestinationMapImageDescription(models.Model):
    program = models.ForeignKey(ProgramPricing, on_delete=models.CASCADE)
    destination_map_image_description = models.TextField()

    def __str__(self):
        return self.program.program_name








