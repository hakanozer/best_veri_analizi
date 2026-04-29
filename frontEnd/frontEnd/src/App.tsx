import { useEffect, useState } from 'react'
import type { IGuc100 } from './models/IGuc100';
import {
  Chart as ChartJS,
  BarElement,
  CategoryScale,
  LinearScale,
  Tooltip,
  Legend
} from 'chart.js';
import { Bar } from 'react-chartjs-2';

ChartJS.register(
  BarElement,
  CategoryScale,
  LinearScale,
  Tooltip,
  Legend
);


function App() {

  const [data, setData] = useState<IGuc100[]>([]);

  const chartData = {
    labels: data.map(item => item.TrafoNo),
    datasets: [
      {
        label: 'Güç',
        data: data.map(item => item.Guc),
      }
    ]
  };

  useEffect(() => {
    setTimeout(() => {
      pullData();
    }, 3000);
  }, [])

  const pullData = () => {
      fetch('http://127.0.0.1:8000/guc1000')
      .then(response => response.json())
      .then(data => setData(data))
      .catch(error => console.error('Error fetching data:', error));
  }

  return (
    <div className="container mt-4">
      <Bar data={chartData} />
      <h4 className="mb-3">Trafo Listesi</h4>

      <div className="table-responsive">
        <table className="table table-striped table-hover table-bordered">
          <thead className="table-dark">
            <tr>
              <th>#</th>
              <th>Proje No</th>
              <th>Sipariş No</th>
              <th>Trafo No</th>
              <th>Tarih</th>
              <th>Güç</th>
              <th>Bobin Tipi</th>
              <th>Çekirdek Ağırlığı</th>
            </tr>
          </thead>
          <tbody>
            {data.map((item, index) => (
              <tr key={item.id}>
                <td>{index + 1}</td>
                <td>{item.ProjeNoMan}</td>
                <td>{item.ProjeSiparisNo}</td>
                <td>{item.TrafoNo}</td>
                <td>
                  {new Date(item.Tarih).toLocaleDateString('tr-TR')}
                </td>
                <td>{item.Guc}</td>
                <td>{item.Bobin}</td>
                <td>{item.CekirdekAgirligi.toFixed(2)}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}

export default App