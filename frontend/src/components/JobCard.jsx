// src/components/JobCard.jsx
import { useState } from 'react';

function JobCard({ id, empresa, cargo, tags, link, favorita: inicial }) {
  const [favorita, setFavorita] = useState(inicial);

  const toggleFavorita = async () => {
    try {
      const response = await fetch(`http://localhost:8000/api/vagas/${id}/favoritar/`, {
        method: 'PATCH',
      });
      const data = await response.json();
      console.log(data.mensagem);
      setFavorita((prev) => !prev);
    } catch (err) {
      console.error('Erro ao favoritar:', err);
    }
  };

  const tagsLimitadas = tags?.slice(0, 6); // Limita a 6 tags

  return (
    <div
      className={`bg-white rounded-xl shadow-md p-4 w-full h-full flex flex-col justify-between relative border-2 ${
        favorita ? 'border-[#13293D]' : 'border-transparent'
      }`}
    >
      <button
        title={favorita ? "Remover dos favoritos" : "Adicionar aos favoritos"}
        onClick={toggleFavorita}
        className="absolute top-3 right-3 text-2xl text-[#13293D] hover:scale-110 transition"
      >
        {favorita ? '★' : '☆'}
      </button>

      <div>
        <h3 className="text-[#13293D] font-bold text-lg">{empresa}</h3>
        <p className="text-[#247BA0] font-semibold">{cargo}</p>
        <div className="flex flex-wrap gap-2 mt-2 max-h-[60px] overflow-y-hidden">
          {tagsLimitadas?.map((tag, index) => (
            <span
              key={index}
              className="bg-[#1B98E0] text-white text-xs px-3 py-1 rounded-full whitespace-nowrap max-w-[120px] overflow-hidden text-ellipsis"
              title={tag}
            >
              {tag}
            </span>
          ))}
        </div>

      </div>

      <div className="flex justify-end gap-2 mt-6">
        <button className="border border-[#13293D] text-[#13293D] font-medium px-3 py-1 rounded-md hover:bg-[#13293D] hover:text-white transition">
          Ver detalhes
        </button>
        <a
          href={link}
          target="_blank"
          rel="noopener noreferrer"
          className="bg-[#006494] text-white font-medium px-3 py-1 rounded-md hover:bg-[#247BA0] transition"
        >
          Acessar vaga
        </a>
      </div>
    </div>
  );
}

export default JobCard;
