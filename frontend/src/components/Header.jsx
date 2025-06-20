import { useState } from 'react';
import axios from 'axios';

function Header() {
  const [palavra, setPalavra] = useState('');
  const [loading, setLoading] = useState(false);

  const buscarVagas = async () => {
    if (!palavra.trim()) return;

    setLoading(true);
    try {
      const response = await axios.post('http://localhost:8000/api/coletar-vagas/', {
        palavra: palavra.trim(),
      });

      console.log('Vagas coletadas com sucesso:', response.data);
      alert('✅ Vagas coletadas com sucesso!');
    } catch (error) {
      console.error('Erro ao coletar vagas:', error);
      alert('❌ Erro ao coletar vagas. Veja o console.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <header className="bg-[#13293D] text-white p-4 flex items-center justify-between shadow-md">
      <h1 className="text-3xl font-bold tracking-wide">AutoJobs</h1>
      <div className="flex gap-2 items-center">
        <input
          type="text"
          placeholder="Buscar vaga..."
          value={palavra}
          onChange={(e) => setPalavra(e.target.value)}
          className="px-4 py-2 rounded-md text-black w-64"
        />
        <button
          onClick={buscarVagas}
          disabled={loading}
          className={`${
            loading ? 'bg-gray-500 cursor-not-allowed' : 'bg-[#006494] hover:bg-[#247BA0]'
          } text-white font-medium px-4 py-2 rounded-md transition`}
        >
          {loading ? 'Buscando...' : 'Buscar'}
        </button>
      </div>
    </header>
  );
}

export default Header;
