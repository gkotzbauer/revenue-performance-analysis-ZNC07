# Urgent Care Revenue Performance Dashboard

A comprehensive web-based dashboard for analyzing urgent care revenue performance data with actionable insights and visualizations.

## Features

- 📊 **Interactive Charts**: Performance distribution, revenue trends, and improvement analysis
- 🎯 **Actionable Insights**: Immediate actions and "Keep It Up" recommendations
- 📈 **Revenue Analysis**: Missed/gained revenue tracking and performance diagnostics
- 🔍 **Advanced Filtering**: Filter by year/week and performance diagnostics
- 📤 **Export Functionality**: Download filtered results as Excel files
- 👥 **User Management**: Admin panel for data updates, regular user view

## Setup Instructions

### For Regular Users
1. Simply open `index.html` in your web browser
2. The dashboard will automatically load the latest data
3. Use the filters to analyze specific time periods or performance categories
4. Export results as needed

### For Administrators
1. Add `?admin=true` to the URL or set `localStorage.setItem('isAdmin', 'true')` in browser console
2. Upload new data files through the admin panel
3. To make data available to all users:
   - Save your Excel file as `revenue-data.xlsx`
   - Place it in the `data/` folder of this repository
   - Commit and push the changes

### Data File Requirements
Your Excel file should contain these columns:
- `Year` - Year of the data
- `Week` - Week number
- `Total Payments` - Actual revenue received
- `Predicted Payments` - Expected revenue
- `Performance Diagnostic` - Over/Average/Under Performed
- `Payment per Visit` - Revenue per patient visit
- `Collection Rate` - Percentage of charges collected
- `Visit Count` - Number of patient visits
- `Charge Amount` - Total charges billed
- `What Went Well` - Semicolon-separated list of positive factors
- `What Can Be Improved` - Semicolon-separated list of improvement areas
- `Aetna Analysis` - Insurance-specific analysis
- `BCBS Analysis` - Insurance-specific analysis

## Usage

### Viewing the Dashboard
1. Open `index.html` in a web browser
2. The dashboard will automatically load with the latest data
3. Use the filters at the top to narrow down your analysis
4. Scroll through the various charts and insights

### Admin Functions
- **Upload New Data**: Use the admin panel to upload updated Excel files
- **Update Repository**: Save files to the `data/` folder to make them available to all users
- **Version Control**: Commit changes to track data updates

### Exporting Results
1. Apply your desired filters
2. Click the "Export to Excel" button at the bottom
3. The filtered data will be downloaded as an Excel file

## Technical Details

- **Frontend**: Pure HTML/CSS/JavaScript with Chart.js for visualizations
- **Data Processing**: Uses SheetJS library for Excel file parsing
- **No Backend Required**: Runs entirely in the browser
- **Responsive Design**: Works on desktop and mobile devices

## File Structure
```
Revenue_Performance_Analysis/
├── index.html              # Main dashboard file
├── data/                   # Data files directory
│   └── revenue-data.xlsx   # Pre-loaded data file
├── README.md              # This file
└── .gitignore             # Git ignore file
```

## Troubleshooting

### Data Not Loading
- Ensure `revenue-data.xlsx` exists in the `data/` folder
- Check that the file format matches the required column structure
- Verify the file is accessible via web server

### Admin Panel Not Showing
- Add `?admin=true` to the URL
- Or run `localStorage.setItem('isAdmin', 'true')` in browser console

### Export Issues
- Ensure you have data loaded before attempting export
- Check browser console for any JavaScript errors
- Try refreshing the page if issues persist

## Version History

- **v4.0**: Added detailed debugging for action item counting
- **v3.0**: Implemented admin panel and user management
- **v2.0**: Enhanced filtering and export functionality
- **v1.0**: Initial dashboard with basic charts and analysis

## Support

For issues or questions, please check the browser console for error messages and ensure all required files are present in the correct locations.
