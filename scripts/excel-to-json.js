// excel-to-json.js
import xlsx from 'xlsx';
import fs from 'fs';
import path from 'path';

const excelPath = path.join(process.cwd(), 'data', 'revenue-data.xlsx');
const jsonPath = path.join(process.cwd(), 'data', 'revenue-data.json');

if (!fs.existsSync(excelPath)) {
  console.error('Excel file not found:', excelPath);
  process.exit(1);
}

const workbook = xlsx.readFile(excelPath);
const firstSheetName = workbook.SheetNames[0];
const worksheet = workbook.Sheets[firstSheetName];
const jsonData = xlsx.utils.sheet_to_json(worksheet);

fs.writeFileSync(jsonPath, JSON.stringify(jsonData, null, 2));
console.log('Successfully updated', jsonPath, 'from', excelPath); 