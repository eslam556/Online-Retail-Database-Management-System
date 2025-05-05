-- Populate the Date Dimension table
DECLARE @StartDate DATE = '1980-01-01';
DECLARE @EndDate DATE = '2025-12-31';
DECLARE @CurrentDate DATE = @StartDate;

-- Common holidays (US-centric, adjust as needed)
DECLARE @NewYearsDay DATE, @IndependenceDay DATE, @ChristmasDay DATE, @LaborDay DATE, 
        @MemorialDay DATE, @ThanksgivingDay DATE, @MLKDay DATE, @PresidentsDay DATE;

WHILE @CurrentDate <= @EndDate
BEGIN
    -- Calculate holidays for the current year
    DECLARE @CurrentYear INT = YEAR(@CurrentDate);
    
    -- Fixed date holidays
    SET @NewYearsDay = DATEFROMPARTS(@CurrentYear, 1, 1);
    SET @IndependenceDay = DATEFROMPARTS(@CurrentYear, 7, 4);
    SET @ChristmasDay = DATEFROMPARTS(@CurrentYear, 12, 25);
    
    -- Floating holidays (US rules)
    -- Martin Luther King Jr. Day (3rd Monday in January)
    SET @MLKDay = DATEADD(DAY, (21 - DATEPART(WEEKDAY, DATEFROMPARTS(@CurrentYear, 1, 1))), DATEFROMPARTS(@CurrentYear, 1, 1));
    
    -- Presidents' Day (3rd Monday in February)
    SET @PresidentsDay = DATEADD(DAY, (21 - DATEPART(WEEKDAY, DATEFROMPARTS(@CurrentYear, 2, 1))), DATEFROMPARTS(@CurrentYear, 2, 1));
    
    -- Memorial Day (last Monday in May)
    SET @MemorialDay = DATEADD(DAY, -((DATEPART(WEEKDAY, DATEFROMPARTS(@CurrentYear, 5, 31)) + 6) % 7), DATEFROMPARTS(@CurrentYear, 5, 31));
    
    -- Labor Day (1st Monday in September)
    SET @LaborDay = DATEADD(DAY, (8 - DATEPART(WEEKDAY, DATEFROMPARTS(@CurrentYear, 9, 1))), DATEFROMPARTS(@CurrentYear, 9, 1));
    
    -- Thanksgiving Day (4th Thursday in November)
    SET @ThanksgivingDay = DATEADD(DAY, (26 - DATEPART(WEEKDAY, DATEFROMPARTS(@CurrentYear, 11, 1))), DATEFROMPARTS(@CurrentYear, 11, 1));
    
    -- Determine if current date is a holiday
    DECLARE @IsHoliday BIT = 0;
    DECLARE @HolidayName VARCHAR(50) = NULL;
    
    IF @CurrentDate = @NewYearsDay 
    BEGIN
        SET @IsHoliday = 1;
        SET @HolidayName = 'New Year''s Day';
    END
    ELSE IF @CurrentDate = @MLKDay 
    BEGIN
        SET @IsHoliday = 1;
        SET @HolidayName = 'Martin Luther King Jr. Day';
    END
    ELSE IF @CurrentDate = @PresidentsDay 
    BEGIN
        SET @IsHoliday = 1;
        SET @HolidayName = 'Presidents'' Day';
    END
    ELSE IF @CurrentDate = @MemorialDay 
    BEGIN
        SET @IsHoliday = 1;
        SET @HolidayName = 'Memorial Day';
    END
    ELSE IF @CurrentDate = @IndependenceDay 
    BEGIN
        SET @IsHoliday = 1;
        SET @HolidayName = 'Independence Day';
    END
    ELSE IF @CurrentDate = @LaborDay 
    BEGIN
        SET @IsHoliday = 1;
        SET @HolidayName = 'Labor Day';
    END
    ELSE IF @CurrentDate = @ThanksgivingDay 
    BEGIN
        SET @IsHoliday = 1;
        SET @HolidayName = 'Thanksgiving Day';
    END
    ELSE IF @CurrentDate = @ChristmasDay 
    BEGIN
        SET @IsHoliday = 1;
        SET @HolidayName = 'Christmas Day';
    END
    
    -- Insert the date record
    INSERT INTO Dim_Date(
        FullDate,
        DayOfWeek,
        DayName,
        DayOfMonth,
        DayOfYear,
        WeekOfYear,
        MonthNumber,
        MonthName,
        Quarter,
        QuarterName,
        Year,
        IsWeekend,
        IsHoliday,
        HolidayName
    )
    VALUES (
        @CurrentDate,
        DATEPART(WEEKDAY, @CurrentDate),
        DATENAME(WEEKDAY, @CurrentDate),
        DATEPART(DAY, @CurrentDate),
        DATEPART(DAYOFYEAR, @CurrentDate),
        DATEPART(WEEK, @CurrentDate),
        DATEPART(MONTH, @CurrentDate),
        DATENAME(MONTH, @CurrentDate),
        DATEPART(QUARTER, @CurrentDate),
        CASE DATEPART(QUARTER, @CurrentDate)
            WHEN 1 THEN 'First'
            WHEN 2 THEN 'Second'
            WHEN 3 THEN 'Third'
            WHEN 4 THEN 'Fourth'
        END,
        YEAR(@CurrentDate),
        CASE WHEN DATEPART(WEEKDAY, @CurrentDate) IN (1, 7) THEN 1 ELSE 0 END,
        @IsHoliday,
        @HolidayName
    );
    
    -- Move to the next date
    SET @CurrentDate = DATEADD(DAY, 1, @CurrentDate);
END
GO

-- Verify the data
SELECT COUNT(*) AS TotalDates FROM Dim_Date;
SELECT MIN(FullDate) AS MinDate, MAX(FullDate) AS MaxDate FROM Dim_Date;
GO